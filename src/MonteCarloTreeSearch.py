from cmath import inf
import copy
import math
import random
from re import L
import pickle
from ultimatetictactoe import *
#Deprecated
class Node:
    def __init__(self, game, parent):
        self.parent = parent
        self.Children = []
        self.game = game
        self.visitCount = 0
        
class MCTS:
    def __init__(self):
        self.root = Node(UltimateTicTacToe(), None)
        self.setChildren(self.root)

    def setChildren(self, node):
        if (len(node.Children) > 0 or node.game.status != ''):
            return
        game = node.game.deepCopy()
        possiblemoves = game.getValidMoves()
        for (bigpos, smallpos) in possiblemoves:
            game.bigmove(bigpos, smallpos)
            node.Children.append(Node(game, node))
            game = node.game.deepCopy()
    
    def selection(self, node):
        while (len(node.Children) > 0):
            maxvalues = []
            maxval = None
            value = None
            for i in range(0, len(node.Children)):
                x = node.Children[i]
                value = 0
                if (x.game.depth % 2 == 0):
                    value = x.game.owins - x.game.xwins
                else:
                    value = x.game.xwins-x.game.owins
                if(x.visitCount == 0):
                    maxval = float(inf)
                    maxvalues.append(i)
                    continue
                UCB = (value/ x.visitCount) + math.sqrt(2)* math.sqrt((math.log(node.visitCount)/ x.visitCount))
                if (maxval == None or UCB > maxval):
                    maxval = UCB
                    maxvalues = []
                    maxvalues.append(i)
                elif (maxval == UCB):
                    maxvalues.append(i)
            node = node.Children[maxvalues[random.randrange(0, len(maxvalues))]]
        return node
    
    def simulateAndBackPropagate(self, node):
        botgame = node.game.deepCopy()
        while (botgame.status == ''):
            possiblemoves = botgame.getValidMoves()
            x = random.randrange(0,len(possiblemoves))
            botgame.bigmove(possiblemoves[x][0], possiblemoves[x][1])
        while (node != None):
            if (botgame.status == 'x'):
                node.game.xwins+=1
            elif(botgame.status == 'o'):
                node.game.owins+=1
            else:
                node.game.ties+=1
            node.visitCount+=1
            node = node.parent
    
    def run(self, node):
        x = self.selection(node)
        self.setChildren(x)
        self.simulateAndBackPropagate(x)

    def search(self, node, runnum):
        for i in range(0, runnum):
            self.run(node)

    def printtree(self, node, indents):
        if (node.visitCount == 0):
            return
        print(indents + "(" + str(node.visitCount) + " " + str(node.game.previousmove) + str(node.game.depth) +" "+ str(node.game.xwins) + " "+ str(node.game.owins) + " " + str(node.game.ties) +")")
        for x in node.Children:
            self.printtree(x, indents+"  ")
    
    def save(self, filename):
        pickle.dump(self.root, open(filename, "wb"))

    def load(self, filename):
        self.root = pickle.load(open(filename, "rb"))

class MCTSBotPlayer:
    def __init__(self, game, mcts):
        self.mcts = mcts
        # mcts.load("C:/Users/Joshua Ni/Documents/UTTTMCTS/MCTS100000.p")
        self.currentgame = game
        self.currentnode = self.mcts.root
    
    def chooseandPlayMove(self):
        if (self.currentgame.status != ''):
            return
        if (self.currentgame.previousmove != None):
            self.follow()
        if(len(self.currentnode.Children) == 0):
            self.mcts.search(self.currentnode, 100)
        maxval = None
        bestpositions = []
        for i in range(0, len(self.currentnode.Children)):
            if (maxval == None or maxval < (self.currentnode.visitCount)):
                maxval = self.currentnode.visitCount
                bestpositions = []
                bestpositions.append(self.currentnode.Children[i].game.previousmove)
            elif(maxval == self.currentnode.visitCount):
                bestpositions.append(self.currentnode.Children[i].game.previousmove)
        x = random.randrange(0, len(bestpositions))
        self.currentgame.bigmove(bestpositions[x][0], bestpositions[x][1])
        self.follow()
        # print("played " + self.player +": " + str(self.currentgame.previousmove))
        
    def follow(self):
        if (len(self.currentnode.Children) == 0 and self.currentnode.game.status == ''):
            self.mcts.search(self.currentnode, 100)
        for i in range(0, len(self.currentnode.Children)):
            if (self.currentgame.previousmove == self.currentnode.Children[i].game.previousmove):
                self.currentnode = self.currentnode.Children[i]
                # print("Followed "+self.player+ ": " + str(self.currentnode.game.previousmove))
                return
        raise Exception("Cannot follow" + str(self.currentgame.previousmove) + str(self.currentnode.game.previousmove))
# def training(runnum):
#     time1 = time.time()
#     mcts = MCTS()
#     mcts.search(mcts.root, runnum)
#     mcts.save("C:/Users/Joshua Ni/Documents/UTTTMCTS/MCTS" + str(runnum) + ".p")
#     time2 = time.time()
#     print("average time for run:" + str((time2-time1)/runnum))
#     print("totaltime:" + str(time2-time1))
#     # mcts.printtree(mcts.root, "")