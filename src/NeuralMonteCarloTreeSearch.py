import copy
import math
import random
import torch
from ultimatetictactoe import UltimateTicTacToe
import numpy as np

class Node:
    def __init__(self, game, parent):
        self.parent = parent
        self.children = []
        self.game = game
        self.visitCount = 0
        self.valueMean = 0.0
        self.value = None
        self.valueSum = 0.0
        self.moveProbability = None
        
class NMCTS:
    def __init__(self, policyNet, device):
        self.root = Node(UltimateTicTacToe(), None)
        self.policyNet = policyNet
        self.device = device

    def expand(self, node):
        if (len(node.children) > 0 or node.game.status != ''):
            return
        game = node.game.deepCopy()
        possibleMoves = game.getValidMoves()
        for (bigPos, smallPos) in possibleMoves:
            game.move(bigPos, smallPos)
            node.children.append(Node(game, node))
            game = node.game.deepCopy()
    
    def selection(self, node):
        while (len(node.children) > 0):
            maxWeightIndices = []
            maxWeight = None
            # value = None
            for i in range(0, len(node.children)):
                child = node.children[i]
                weight = (-child.valueMean) + 2.0*max(0.01, child.moveProbability) * math.sqrt(node.visitCount) / (child.visitCount + 1)
                if (maxWeight == None or weight > maxWeight):
                    maxWeight = weight
                    maxWeightIndices = []
                    maxWeightIndices.append(i)
                elif (maxWeight == weight):
                    maxWeightIndices.append(i)
            node = node.children[maxWeightIndices[random.randrange(0, len(maxWeightIndices))]]
        return node

    def evaluate(self, node):
        if (node.game.status != ""):
            if (node.game.status == "t"):
                node.value = 0.0
            else:
                node.value = -1.0
            return
        input4x9x9 = self.getInput4x9x9(node.game)
        input1x4x9x9 = np.expand_dims(input4x9x9, axis=0)
        input1x4x9x9 = torch.from_numpy(input1x4x9x9)
        input1x4x9x9 = input1x4x9x9.to(device=torch.device(self.device), dtype=torch.float32)
        with torch.no_grad():
            policyLogits, actionValues, stateValue = self.policyNet(input1x4x9x9)
        policyLogitsTensor = policyLogits[0].cpu()
        policyLogitsList = []
        for childNode in node.children:
            actionIndex = childNode.game.previousMove
            i = 3*int((actionIndex[0]-1)/3) + int((actionIndex[1]-1)/3)
            j = 3*((actionIndex[0]-1)%3) + (actionIndex[1]-1)%3
            actionLogit = policyLogitsTensor[i, j].item()
            policyLogitsList.append(actionLogit)
        policyLogitsTensor = torch.tensor(policyLogitsList)
        policyProbasTensor = torch.softmax(policyLogitsTensor, dim=0)
        for i, childNode in enumerate(node.children):
            childNode.moveProbability = policyProbasTensor[i].item()
        stateValue = stateValue[0].item()
        node.value = stateValue

    def getInput4x9x9(self, uttt):
            input = np.zeros(shape=(4, 9, 9), dtype=np.int8)
            # 0: current player's symbols
            # 1: opponent's symbols
            if uttt.nextPlayer() == 1:
                x_i, o_i = 0, 1
            elif uttt.nextPlayer() == 2:
                x_i, o_i = 1, 0
            tempBigBoard = [0]*9
            for i in range(0, 9):
                tempBigBoard[i] = copy.deepcopy(uttt.bigBoard[i].board)
            for i in range(0, 9):
                for j in range(0,9):
                    x = 3*int(i/3) + int(j/3)
                    y = 3*(i%3) + j%3
                    if tempBigBoard[x][y] == 1:
                        input[x_i, i, j] = 1
                    elif tempBigBoard[x][y] == 2:
                        input[o_i, i, j] = 1
            # 2: fill 1 or -1 depending on the current player's symbol (X or O)
            if uttt.nextPlayer() == 1:
                input[2].fill(1)
            elif uttt.nextPlayer()==2:
                input[2].fill(-1)
            # 3: current player's legal moves
            for (x,y) in uttt.getValidMoves():
                i = 3*int((x-1)/3) + int((y-1)/3)
                j = 3*((x-1)%3) + (y-1)%3
                input[3, i, j] = 1
            return input

    def backPropagate(self, node, stateVal, root):
        sign = 1
        while (node != root.parent):
            node.visitCount+=1
            node.valueSum += sign * stateVal
            node.valueMean = node.valueSum/node.visitCount
            node = node.parent
            sign*=-1

    def simulate(self, node):
        currentNode = self.selection(node)
        self.expand(currentNode)
        self.evaluate(currentNode)
        self.backPropagate(currentNode, currentNode.value, node)

    def search(self, node, runNum):
        trueRunNum = runNum - node.visitCount
        # print("searching" + str(node.game.previousMove))
        for i in range(0, trueRunNum):
            self.simulate(node)