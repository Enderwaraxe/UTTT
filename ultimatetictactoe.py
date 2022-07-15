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
        self.status = "incomplete"
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
                self.status = "xwins"
            else:
                self.status = "owins"
        elif len(self.trace) >= 9:
            self.status = "tie"

    def reset(self):
        self.board = [0]*9
        self.status = "incomplete"
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
        self.trace = []
        self.status = ''
        self.xwins = 0
        self.owins = 0
        self.ties = 0

    def reset(self):
        self.bigboard = []
        for i in range(0, 9):
            self.bigboard.append(BaseTicTacToe())
        self.trace = []
        self.status = ''
    def isWon(self):
        if ((self.bigboard[0].getStatus() == self.bigboard[1].getStatus() and self.bigboard[1].getStatus() == self.bigboard[2].getStatus() and self.bigboard[0].getStatus() !=  "incomplete" and self.bigboard[0].getStatus() !=  "tie") or (self.bigboard[3].getStatus() == self.bigboard[4].getStatus() and self.bigboard[4].getStatus() == self.bigboard[5].getStatus() and self.bigboard[3].getStatus() != "incomplete" and self.bigboard[3].getStatus() != "tie") or (self.bigboard[6].getStatus() == self.bigboard[7].getStatus() and self.bigboard[7].getStatus() == self.bigboard[8].getStatus() and self.bigboard[6].getStatus() != "incomplete" and self.bigboard[6].getStatus() != "tie") or (self.bigboard[0].getStatus() == self.bigboard[3].getStatus() and self.bigboard[3].getStatus() == self.bigboard[6].getStatus() and self.bigboard[0].getStatus() != "incomplete" and self.bigboard[0].getStatus() != "tie") or (self.bigboard[1].getStatus() == self.bigboard[4].getStatus() and self.bigboard[4].getStatus() == self.bigboard[7].getStatus() and self.bigboard[1].getStatus() != "incomplete" and self.bigboard[1].getStatus() != "tie") or (self.bigboard[2].getStatus() == self.bigboard[5].getStatus() and self.bigboard[5].getStatus() == self.bigboard[8].getStatus() and self.bigboard[2].getStatus() != "incomplete" and self.bigboard[2].getStatus() != "tie") or (self.bigboard[0].getStatus() == self.bigboard[4].getStatus() and self.bigboard[4].getStatus() == self.bigboard[8].getStatus() and self.bigboard[0].getStatus() != "incomplete" and self.bigboard[0].getStatus() != "tie") or (self.bigboard[2].getStatus() == self.bigboard[4].getStatus() and self.bigboard[4].getStatus() == self.bigboard[6].getStatus() and self.bigboard[2].getStatus() != "incomplete" and self.bigboard[2].getStatus() != "tie")):
            return True
        return False
    
    def bigjustplayed(self):
        if (len(self.trace)%2==1):
            return 1
        else:
            return 2

    def bignextPlayer(self):
        if (len(self.trace)%2 == 0):
            return 1
        else:
            return 2
    
    def bigmove(self, largeboardpos, smallboardpos):
        # smallboardpos = int(input("1-9 "+ str(self.bignextPlayer()) + " small " + str(largeboardpos) + " "))
        if (( len(self.trace) == 0) or (self.isBoardFinished(self.trace[len(self.trace)-1][1]))):
            while (smallboardpos < 1 or smallboardpos > 9 or self.bigboard[largeboardpos-1].isTaken(smallboardpos) or largeboardpos < 1 or largeboardpos > 9 or self.isBoardFinished(largeboardpos)):    
                # smallboardpos = int(input("1-9 "+ str(self.bignextPlayer()) + " small " + str(largeboardpos) + " "))
                # smallboardpos = random.randrange(1, 10)
                # largeboardpos = random.randrange(1,10)
                raise Exception("Invalid pos "+ str(largeboardpos) + " " + str(smallboardpos))
        else:
            largeboardpos = self.trace[len(self.trace)-1][1]
            while (smallboardpos < 1 or smallboardpos > 9 or self.bigboard[largeboardpos-1].isTaken(smallboardpos)):    
                # smallboardpos = int(input("1-9 "+ str(self.bignextPlayer()) + " small " + str(largeboardpos) + " "))
                # smallboardpos = random.randrange(1, 10)
                raise Exception("Invalid pos "+ str(largeboardpos) + " " + str(smallboardpos))
        
        
        self.bigboard[largeboardpos-1].movesmallboard(smallboardpos, self.bignextPlayer())
        self.trace.append((largeboardpos, smallboardpos))

        if (self.isWon()):
            if (self.bigjustplayed() == 1):
                self.status = "xwins"
                # print("X wins!")
            else:
                self.status = "owins"
                # print("O wins!")
        #TODO change to isboardfinished
        elif (self.bigboard[0].getStatus() != "incomplete" and self.bigboard[1].getStatus() != "incomplete" and self.bigboard[2].getStatus() != "incomplete" and self.bigboard[3].getStatus() != "incomplete" and self.bigboard[4].getStatus() != "incomplete" and self.bigboard[5].getStatus() != "incomplete" and self.bigboard[6].getStatus() != "incomplete" and self.bigboard[7].getStatus() != "incomplete" and self.bigboard[8].getStatus() != "incomplete"):
            self.status = "tie"
            # print("Tie!")
    
    def isBoardFinished(self, pos):
        if (self.bigboard[pos-1].getStatus() == "incomplete"):
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

    def setState(self, bigboard, trace, status):
        for i in range(0, 9):
            self.bigboard[i] = bigboard[i].deepCopys()
        self.trace = copy.deepcopy(trace)
        self.status = copy.deepcopy(status)

    def deepCopy(self):
        copy = UltimateTicTacToe()
        copy.setState(self.bigboard, self.trace, self.status)
        return copy

    def getValidMoves(self):
        possiblemoves = []
        if (len(self.trace) == 0 or self.isBoardFinished(self.trace[len(self.trace)-1][1])):
            for i in range(1, 10):
                bigpos = i
                for j in range(1,10):
                    if ((not self.bigboard[bigpos-1].isTaken(j)) and (not self.isBoardFinished(bigpos))):
                        possiblemoves.append((bigpos, j))
        else:
            bigpos = self.trace[len(self.trace)-1][1]
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
                if (len(node.game.trace)%2 == 0):
                    value = node.game.owins - node.game.xwins
                else:
                    value = node.game.xwins-node.game.owins
                if(x.visitCount == 0):
                    maxval = float(inf)
                    maxvalues.append(i)
                    continue
                UCB = (value/ x.visitCount) + 2* (math.log(node.visitCount)/ x.visitCount)**(1/2)
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
            if (botgame.status == 'xwins'):
                node.game.xwins+=1
            elif(botgame.status == 'owins'):
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
        time1 = time.time()
        for i in range(0, runnum):
            self.run(node)
        time2 = time.time()
        print("average time for run:" + str((time2-time1)/runnum))
        print("totaltime:" + str(time2-time1))

    def printtree(self, node, indents):
        if (node.visitCount == 0):
            return
        print(indents + "(" + str(node.visitCount) + " " + str(node.game.trace) +" "+ str(node.game.xwins) + " "+ str(node.game.owins) + " " + str(node.game.ties) +")")
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
            if (self.player == 'x'):
                if (maxval == None or maxval < (self.currentnode.game.xwins-self.currentnode.game.owins)/self.currentnode.visitCount):
                    maxval = (self.currentnode.game.xwins-self.currentnode.game.owins)/self.currentnode.visitCount
                    bestpositions = []
                    bestpositions.append(self.currentnode.Children[i].game.trace[len(self.currentnode.Children[i].game.trace)-1])
                elif(maxval == (self.currentnode.game.xwins-self.currentnode.game.owins)/self.currentnode.visitCount):
                    bestpositions.append(self.currentnode.Children[i].game.trace[len(self.currentnode.Children[i].game.trace)-1])
            else:
                if (maxval == None or maxval < (self.currentnode.game.owins-self.currentnode.game.xwins)/self.currentnode.visitCount):
                    maxval = (self.currentnode.game.owins-self.currentnode.game.xwins)/self.currentnode.visitCount
                    bestpositions = []
                    bestpositions.append(self.currentnode.Children[i].game.trace[len(self.currentnode.Children[i].game.trace)-1])
                elif(maxval == (self.currentnode.game.owins-self.currentnode.game.xwins)/self.currentnode.visitCount):
                    bestpositions.append(self.currentnode.Children[i].game.trace[len(self.currentnode.Children[i].game.trace)-1])
        x = random.randrange(0, len(bestpositions))
        self.currentgame.bigmove(bestpositions[x][0], bestpositions[x][1])
        # print("played " + self.player +": " + str(self.currentgame.trace))
        
    def follow(self):
        if (len(self.currentnode.Children) == 0 and self.currentnode.game.status == ''):
            self.mcts.search(self.currentnode, 100)
        for i in range(0, len(self.currentnode.Children)):
            if (self.currentgame.trace[-1] == self.currentnode.Children[i].game.trace[-1]):
                self.currentnode = self.currentnode.Children[i]
                # print("Followed "+self.player+ ": " + str(self.currentnode.game.trace))
                return
        raise Exception("Cannot follow" + str(self.currentgame.trace) + str(self.currentnode.game.trace))

class RandomPlayer():
    def __init__(self, game):
        self.currentgame = game

    def chooseandPlayMove(self):
        possiblemoves = self.currentgame.getValidMoves()
        x = random.randrange(0,len(possiblemoves))
        self.currentgame.bigmove(possiblemoves[x][0], possiblemoves[x][1])

    def follow(self):
        pass

ultimategame = UltimateTicTacToe()
# mcts = MCTS()
# mcts.search(mcts.root, 1000000)
# mcts.save("C:/Users/Joshua Ni/Documents/UTTTMCTS/Test.p")
mcts1 = MCTS()
mcts2 = MCTS()
mcts1.load("C:/Users/Joshua Ni/Documents/UTTTMCTS/1000MCTS.p")
mcts2.load("C:/Users/Joshua Ni/Documents/UTTTMCTS/2000MCTS.p")
isOBot = True
isXBot = True
isOsTurn = False
for i in range(0, 20):
    BotOPlayer = MCTSBotPlayer('o', ultimategame, mcts2)
    BotXPlayer = MCTSBotPlayer('x', ultimategame, mcts1)
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
    if (ultimategame.status == 'xwins'):
        # print("X Wins!")
        ultimategame.xwins+=1
    elif (ultimategame.status == 'owins'):
        # print("O Wins!")
        ultimategame.owins+=1
    elif (ultimategame.status == 'tie'):
        # print("Tie!")
        ultimategame.ties+=1
    ultimategame.reset()
    
print(str(ultimategame.xwins) + " " + str(ultimategame.owins) + " " + str(ultimategame.ties))
# # mcts.printtree(mcts.root, "")