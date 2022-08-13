import copy
import random
#replace x and o with 1 and 2
class TicTacToe:
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
  
    def move(self, move, player):
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

    def getBoard(self):
        return self.board

    def setState(self, board, trace, status):
        self.board = copy.deepcopy(board)
        self.trace = copy.deepcopy(trace)
        self.status = copy.deepcopy(status)
    
    def deepCopys(self):
        copy = TicTacToe()
        copy.setState(self.board, self.trace, self.status)
        return copy

class UltimateTicTacToe:
    def __init__(self):
        self.bigBoard = []
        for i in range(0, 9):
            self.bigBoard.append(TicTacToe())
        self.previousMove = None
        self.depth = 0
        self.status = ''
        self.xWins = 0
        self.oWins = 0
        self.ties = 0

    def reset(self):
        self.bigBoard = []
        for i in range(0, 9):
            self.bigBoard.append(TicTacToe())
        self.previousMove = None
        self.status = ''
        self.depth = 0
        
    def isWon(self):
        if ((self.bigBoard[0].getStatus() == self.bigBoard[1].getStatus() and self.bigBoard[1].getStatus() == self.bigBoard[2].getStatus() and self.bigBoard[0].getStatus() !=  "" and self.bigBoard[0].getStatus() !=  "t") or (self.bigBoard[3].getStatus() == self.bigBoard[4].getStatus() and self.bigBoard[4].getStatus() == self.bigBoard[5].getStatus() and self.bigBoard[3].getStatus() != "" and self.bigBoard[3].getStatus() != "t") or (self.bigBoard[6].getStatus() == self.bigBoard[7].getStatus() and self.bigBoard[7].getStatus() == self.bigBoard[8].getStatus() and self.bigBoard[6].getStatus() != "" and self.bigBoard[6].getStatus() != "t") or (self.bigBoard[0].getStatus() == self.bigBoard[3].getStatus() and self.bigBoard[3].getStatus() == self.bigBoard[6].getStatus() and self.bigBoard[0].getStatus() != "" and self.bigBoard[0].getStatus() != "t") or (self.bigBoard[1].getStatus() == self.bigBoard[4].getStatus() and self.bigBoard[4].getStatus() == self.bigBoard[7].getStatus() and self.bigBoard[1].getStatus() != "" and self.bigBoard[1].getStatus() != "t") or (self.bigBoard[2].getStatus() == self.bigBoard[5].getStatus() and self.bigBoard[5].getStatus() == self.bigBoard[8].getStatus() and self.bigBoard[2].getStatus() != "" and self.bigBoard[2].getStatus() != "t") or (self.bigBoard[0].getStatus() == self.bigBoard[4].getStatus() and self.bigBoard[4].getStatus() == self.bigBoard[8].getStatus() and self.bigBoard[0].getStatus() != "" and self.bigBoard[0].getStatus() != "t") or (self.bigBoard[2].getStatus() == self.bigBoard[4].getStatus() and self.bigBoard[4].getStatus() == self.bigBoard[6].getStatus() and self.bigBoard[2].getStatus() != "" and self.bigBoard[2].getStatus() != "t")):
            return True
        return False
    
    def isDraw(self):
        return self.bigBoard[0].getStatus() != "" and self.bigBoard[1].getStatus() != "" and self.bigBoard[2].getStatus() != "" and self.bigBoard[3].getStatus() != "" and self.bigBoard[4].getStatus() != "" and self.bigBoard[5].getStatus() != "" and self.bigBoard[6].getStatus() != "" and self.bigBoard[7].getStatus() != "" and self.bigBoard[8].getStatus() != ""
    
    def justPlayed(self):
        if (self.depth%2==1):
            return 1
        else:
            return 2

    def nextPlayer(self):
        if (self.depth%2 == 0):
            return 1
        else:
            return 2
    
    def move(self, largeBoardPos, smallBoardPos):
        if ((self.depth == 0) or (self.isBoardFinished(self.previousMove[1]))):
            if (smallBoardPos < 1 or smallBoardPos > 9 or self.bigBoard[largeBoardPos-1].isTaken(smallBoardPos) or largeBoardPos < 1 or largeBoardPos > 9 or self.isBoardFinished(largeBoardPos)):    
                raise Exception("Invalid pos "+ str(largeBoardPos) + " " + str(smallBoardPos))
        else:
            largeBoardPos = self.previousMove[1]
            if (smallBoardPos < 1 or smallBoardPos > 9 or self.bigBoard[largeBoardPos-1].isTaken(smallBoardPos)):    
                raise Exception("Invalid pos "+ str(largeBoardPos) + " " + str(smallBoardPos))
        self.bigBoard[largeBoardPos-1].move(smallBoardPos, self.nextPlayer())
        self.previousMove = (largeBoardPos, smallBoardPos)
        self.depth+=1
        if (self.isWon()):
            if (self.justPlayed() == 1):
                self.status = "x"
                # print("X wins!")
            else:
                self.status = "o"
                # print("O wins!")
        elif(self.isDraw()):
            self.status = "t"
            # print("Tie!")
    
    def isBoardFinished(self, pos):
        if (self.bigBoard[pos-1].getStatus() == ""):
            return False
        return True
    
    def printBoard(self):
        x1 = self.bigBoard[0].getBoard()
        x2 = self.bigBoard[1].getBoard()
        x3 = self.bigBoard[2].getBoard()
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
        x1 = self.bigBoard[3].getBoard()
        x2 = self.bigBoard[4].getBoard()
        x3 = self.bigBoard[5].getBoard()
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
        x1 = self.bigBoard[6].getBoard()
        x2 = self.bigBoard[7].getBoard()
        x3 = self.bigBoard[8].getBoard()
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
    
    def getBoard(self):
        return self.bigBoard

    def deepCopy(self):
        copys = UltimateTicTacToe()
        for i in range(0, 9):
            copys.bigBoard[i] = self.bigBoard[i].deepCopys()
        copys.status = copy.deepcopy(self.status)
        copys.depth = self.depth
        copys.previousMove = copy.deepcopy(self.previousMove)
        return copys

    def getValidMoves(self):
        possibleMoves = []
        if (self.status !=''):
            return possibleMoves
        if (self.depth == 0 or self.isBoardFinished(self.previousMove[1])):
            for i in range(1, 10):
                bigPos = i
                for j in range(1,10):
                    if ((not self.bigBoard[bigPos-1].isTaken(j)) and (not self.isBoardFinished(bigPos))):
                        possibleMoves.append((bigPos, j))
        else:
            bigPos = self.previousMove[1]
            for i in range(1, 10):
                if ((not self.bigBoard[bigPos-1].isTaken(i))):
                    possibleMoves.append((bigPos, i))
        return possibleMoves