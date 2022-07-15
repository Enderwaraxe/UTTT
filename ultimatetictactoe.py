from cmath import inf
import copy
import math
import random
from re import L
import time
import pickle
#replace x and o with 1 and 2
class BaseTicTacToe:
    def __init__(self):
        self.trace = []
        self.board = [0]*9
        self.status = ""
    def isBoardWon(self):
        if ((self.board[0] == self.board[1] and self.board[1] == self.board[2] and self.board[0] != 0) or (self.board[3] == self.board[4] and self.board[4] == self.board[5] and self.board[3] != 0) or (self.board[6] == self.board[7] and self.board[7] == self.board[8] and self.board[6] != 0) or (self.board[0] == self.board[3] and self.board[3] == self.board[6] and self.board[0] != 0) or (self.board[1] == self.board[4] and self.board[4] == self.board[7] and self.board[1] != 0) or (self.board[2] == self.board[5] and self.board[5] == self.board[8] and self.board[2] != 0) or (self.board[0] == self.board[4] and self.board[4] == self.board[8] and self.board[0] != 0) or (self.board[2] == self.board[4] and self.board[4] == self.board[6] and self.board[2] != 0)):
            return True
        return False

    def getStatus(self):
        return self.status
  
    def movesmallboard(self, move, player):
        #move is position 1-9, player is who, x = 1, o = 2
        self.trace.append(move)
        self.board[move-1] = player
        if (self.isBoardWon()):
            if (player == 1):
                self.status = "x"
            else:
                self.status = "o"
        elif len(self.trace) >= 9:
            self.status = "t"

    def reset(self):
        self.board = [0]*9
        self.status = ""
        self.trace.clear()
        
    def isTaken(self, pos):
        if (self.board[pos-1] == 0):
            return False
        return True

    def getboard(self):
        return self.board

    def setState(self, board, trace, status):
        self.board = copy.deepcopy(board)
        self.trace = copy.deepcopy(trace)
        self.status = copy.deepcopy(status)
    
    def deepCopys(self):
        copy = BaseTicTacToe()
        copy.setState(self.board, self.trace, self.status)
        return copy

class UltimateTicTacToe:
    def __init__(self):
        self.bigboard = []
        for i in range(0, 9):
            self.bigboard.append(BaseTicTacToe())
        self.previousmove = None
        self.depth = 0
        self.status = ''
        self.xwins = 0
        self.owins = 0
        self.ties = 0

    def reset(self):
        self.bigboard = []
        for i in range(0, 9):
            self.bigboard.append(BaseTicTacToe())
        self.previousmove = None
        self.status = ''
        self.depth = 0
    def isWon(self):
        if ((self.bigboard[0].getStatus() == self.bigboard[1].getStatus() and self.bigboard[1].getStatus() == self.bigboard[2].getStatus() and self.bigboard[0].getStatus() !=  "" and self.bigboard[0].getStatus() !=  "t") or (self.bigboard[3].getStatus() == self.bigboard[4].getStatus() and self.bigboard[4].getStatus() == self.bigboard[5].getStatus() and self.bigboard[3].getStatus() != "" and self.bigboard[3].getStatus() != "t") or (self.bigboard[6].getStatus() == self.bigboard[7].getStatus() and self.bigboard[7].getStatus() == self.bigboard[8].getStatus() and self.bigboard[6].getStatus() != "" and self.bigboard[6].getStatus() != "t") or (self.bigboard[0].getStatus() == self.bigboard[3].getStatus() and self.bigboard[3].getStatus() == self.bigboard[6].getStatus() and self.bigboard[0].getStatus() != "" and self.bigboard[0].getStatus() != "t") or (self.bigboard[1].getStatus() == self.bigboard[4].getStatus() and self.bigboard[4].getStatus() == self.bigboard[7].getStatus() and self.bigboard[1].getStatus() != "" and self.bigboard[1].getStatus() != "t") or (self.bigboard[2].getStatus() == self.bigboard[5].getStatus() and self.bigboard[5].getStatus() == self.bigboard[8].getStatus() and self.bigboard[2].getStatus() != "" and self.bigboard[2].getStatus() != "t") or (self.bigboard[0].getStatus() == self.bigboard[4].getStatus() and self.bigboard[4].getStatus() == self.bigboard[8].getStatus() and self.bigboard[0].getStatus() != "" and self.bigboard[0].getStatus() != "t") or (self.bigboard[2].getStatus() == self.bigboard[4].getStatus() and self.bigboard[4].getStatus() == self.bigboard[6].getStatus() and self.bigboard[2].getStatus() != "" and self.bigboard[2].getStatus() != "t")):
            return True
        return False
    
    def bigjustplayed(self):
        if (self.depth%2==1):
            return 1
        else:
            return 2

    def bignextPlayer(self):
        if (self.depth%2 == 0):
            return 1
        else:
            return 2
    
    def bigmove(self, largeboardpos, smallboardpos):
        # smallboardpos = int(input("1-9 "+ str(self.bignextPlayer()) + " small " + str(largeboardpos) + " "))
        if ((self.depth == 0) or (self.isBoardFinished(self.previousmove[1]))):
            while (smallboardpos < 1 or smallboardpos > 9 or self.bigboard[largeboardpos-1].isTaken(smallboardpos) or largeboardpos < 1 or largeboardpos > 9 or self.isBoardFinished(largeboardpos)):    
                # smallboardpos = int(input("1-9 "+ str(self.bignextPlayer()) + " small " + str(largeboardpos) + " "))
                # smallboardpos = random.randrange(1, 10)
                # largeboardpos = random.randrange(1,10)
                raise Exception("Invalid pos "+ str(largeboardpos) + " " + str(smallboardpos))
        else:
            largeboardpos = self.previousmove[1]
            while (smallboardpos < 1 or smallboardpos > 9 or self.bigboard[largeboardpos-1].isTaken(smallboardpos)):    
                # smallboardpos = int(input("1-9 "+ str(self.bignextPlayer()) + " small " + str(largeboardpos) + " "))
                # smallboardpos = random.randrange(1, 10)
                raise Exception("Invalid pos "+ str(largeboardpos) + " " + str(smallboardpos))
        self.bigboard[largeboardpos-1].movesmallboard(smallboardpos, self.bignextPlayer())
        self.previousmove = (largeboardpos, smallboardpos)
        self.depth+=1

        if (self.isWon()):
            if (self.bigjustplayed() == 1):
                self.status = "x"
                # print("X wins!")
            else:
                self.status = "o"
                # print("O wins!")
        #TODO change to isboardfinished
        elif (self.bigboard[0].getStatus() != "" and self.bigboard[1].getStatus() != "" and self.bigboard[2].getStatus() != "" and self.bigboard[3].getStatus() != "" and self.bigboard[4].getStatus() != "" and self.bigboard[5].getStatus() != "" and self.bigboard[6].getStatus() != "" and self.bigboard[7].getStatus() != "" and self.bigboard[8].getStatus() != ""):
            self.status = "t"
            # print("Tie!")
    
    def isBoardFinished(self, pos):
        if (self.bigboard[pos-1].getStatus() == ""):
            return False
        return True
    
    def printBoard(self):
        x1 = self.bigboard[0].getboard()
        x2 = self.bigboard[1].getboard()
        x3 = self.bigboard[2].getboard()
        for i in range(0, 9):
            if (i < 3):
                print(x1[i], end = '')
            elif (i >= 3 and i < 6):
                print(x2[i%3], end = '')
            elif (i>= 6):
                print(x3[i%6],end = '')
            if (i == 2 or i == 5):
                print("|", end = '')
        print()
        for i in range(0, 9):
            if (i < 3):
                print(x1[i+3], end = '')
            elif (i >= 3 and i < 6):
                print(x2[i%3+3], end = '')
            elif (i>= 6):
                print(x3[i%6+3],end = '')
            if (i == 2 or i == 5):
                print("|", end = '')
        print()
        for i in range(0, 9):
            if (i < 3):
                print(x1[i+6], end = '')
            elif (i >= 3 and i < 6):
                print(x2[i%3+6], end = '')
            elif (i>= 6):
                print(x3[i%6+6],end = '')
            if (i == 2 or i == 5):
                print("|", end = '')
        print()
        print("-----------")
        x1 = self.bigboard[3].getboard()
        x2 = self.bigboard[4].getboard()
        x3 = self.bigboard[5].getboard()
        for i in range(0, 9):
            if (i < 3):
                print(x1[i], end = '')
            elif (i >= 3 and i < 6):
                print(x2[i%3], end = '')
            elif (i>= 6):
                print(x3[i%6],end = '')
            if (i == 2 or i == 5):
                print("|", end = '')
        print()
        for i in range(0, 9):
            if (i < 3):
                print(x1[i+3], end = '')
            elif (i >= 3 and i < 6):
                print(x2[i%3+3], end = '')
            elif (i>= 6):
                print(x3[i%6+3],end = '')
            if (i == 2 or i == 5):
                print("|", end = '')
        print()
        for i in range(0, 9):
            if (i < 3):
                print(x1[i+6], end = '')
            elif (i >= 3 and i < 6):
                print(x2[i%3+6], end = '')
            elif (i>= 6):
                print(x3[i%6+6],end = '')
            if (i == 2 or i == 5):
                print("|", end = '')
        print()
        print("-----------")
        x1 = self.bigboard[6].getboard()
        x2 = self.bigboard[7].getboard()
        x3 = self.bigboard[8].getboard()
        for i in range(0, 9):
            if (i < 3):
                print(x1[i], end = '')
            elif (i >= 3 and i < 6):
                print(x2[i%3], end = '')
            elif (i>= 6):
                print(x3[i%6],end = '')
            if (i == 2 or i == 5):
                print("|", end = '')
        print()
        for i in range(0, 9):
            if (i < 3):
                print(x1[i+3], end = '')
            elif (i >= 3 and i < 6):
                print(x2[i%3+3], end = '')
            elif (i>= 6):
                print(x3[i%6+3],end = '')
            if (i == 2 or i == 5):
                print("|", end = '')
        print()
        for i in range(0, 9):
            if (i < 3):
                print(x1[i+6], end = '')
            elif (i >= 3 and i < 6):
                print(x2[i%3+6], end = '')
            elif (i>= 6):
                print(x3[i%6+6],end = '')
            if (i == 2 or i == 5):
                print("|", end = '')
        print()
    
    def getboard(self):
        return self.bigboard

    def deepCopy(self):
        copys = UltimateTicTacToe()
        for i in range(0, 9):
            copys.bigboard[i] = self.bigboard[i].deepCopys()
        copys.status = copy.deepcopy(self.status)
        copys.depth = self.depth
        copys.previousmove = copy.deepcopy(self.previousmove)
        return copys

    def getValidMoves(self):
        possiblemoves = []
        if (self.depth == 0 or self.isBoardFinished(self.previousmove[1])):
            for i in range(1, 10):
                bigpos = i
                for j in range(1,10):
                    if ((not self.bigboard[bigpos-1].isTaken(j)) and (not self.isBoardFinished(bigpos))):
                        possiblemoves.append((bigpos, j))
        else:
            bigpos = self.previousmove[1]
            for i in range(1, 10):
                if ((not self.bigboard[bigpos-1].isTaken(i))):
                    possiblemoves.append((bigpos, i))
        return possiblemoves

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
    def __init__(self, player, game, mcts):
        self.mcts = mcts
        self.player = player
        self.currentgame = game
        self.currentnode = self.mcts.root
    
    def chooseandPlayMove(self):
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

class RandomPlayer():
    def __init__(self, game):
        self.currentgame = game

    def chooseandPlayMove(self):
        possiblemoves = self.currentgame.getValidMoves()
        x = random.randrange(0,len(possiblemoves))
        self.currentgame.bigmove(possiblemoves[x][0], possiblemoves[x][1])

    def follow(self):
        pass

def playgame():
    ultimategame = UltimateTicTacToe()
    mcts1 = MCTS()
    mcts2 = MCTS()
    mcts1.load("C:/Users/Joshua Ni/Documents/UTTTMCTS/MCTS100000.p")
    # mcts2.load("C:/Users/Joshua Ni/Documents/UTTTMCTS/MCTS100000.p")
    isOBot = True
    isXBot = True
    isOsTurn = False
    for i in range(0, 40):
        # BotOPlayer = MCTSBotPlayer('o', ultimategame, mcts2)
        BotXPlayer = MCTSBotPlayer('x', ultimategame, mcts1)
        BotOPlayer = RandomPlayer(ultimategame)
        # BotXPlayer = RandomPlayer(ultimategame)
        while(ultimategame.status == ''):
            print("\033c", end = '')
            ultimategame.printBoard()
            if (isOsTurn):
                if (isOBot):
                    BotOPlayer.chooseandPlayMove()
                    BotOPlayer.follow()
                else:
                    print("Enter big pos and small pos ")
                    bigpos, smallpos = int(input().split())
                    ultimategame.bigmove(bigpos, smallpos)
                if (isXBot):
                    BotXPlayer.follow()
            else:
                if (isXBot):
                    BotXPlayer.chooseandPlayMove()
                    BotXPlayer.follow()
                else:
                    print("Enter big pos and small pos ")
                    bigpos, smallpos = int(input().split())
                    ultimategame.bigmove(bigpos, smallpos)
                if (isOBot):
                    BotOPlayer.follow()
            isOsTurn = not isOsTurn
        if (ultimategame.status == 'x'):
            # print("X Wins!")
            ultimategame.xwins+=1
        elif (ultimategame.status == 'o'):
            # print("O Wins!")
            ultimategame.owins+=1
        elif (ultimategame.status == 't'):
            # print("Tie!")
            ultimategame.ties+=1
        ultimategame.reset()
        
    print(str(ultimategame.xwins) + " " + str(ultimategame.owins) + " " + str(ultimategame.ties))
    
def training(runnum):
    time1 = time.time()
    mcts = MCTS()
    mcts.search(mcts.root, runnum)
    mcts.save("C:/Users/Joshua Ni/Documents/UTTTMCTS/MCTS" + str(runnum) + ".p")
    time2 = time.time()
    print("average time for run:" + str((time2-time1)/runnum))
    print("totaltime:" + str(time2-time1))
    # mcts.printtree(mcts.root, "")

training(1000000)
# playgame()