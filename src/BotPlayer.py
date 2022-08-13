import random
from NeuralMonteCarloTreeSearch import NMCTS
class NMCTSBotPlayer:
    def __init__(self, game, policyNet, runNum):
        self.nmcts = NMCTS(policyNet)
        self.currentGame = game
        self.currentNode = self.nmcts.root
        self.runNum = runNum
    
    def move(self):
        if (self.currentGame.status != ''):
            return
        if (self.currentGame.previousMove != None):
            self.follow()
        self.nmcts.search(self.currentNode, self.runNum)
        topProb = None
        bestPositions = []
        # print(str(self.currentNode.game.previousMove) + ": " +str(self.currentNode.visitCount))
        for i in range(0, len(self.currentNode.children)):
            child = self.currentNode.children[i]
            probability = (child.visitCount + child.moveProbability * max(0, -0.1 * self.currentNode.visitCount + 100))/(self.currentNode.visitCount +  max(0, -0.1 * self.currentNode.visitCount + 100) -1)
            if (topProb == None or topProb < (probability)):
                topProb = probability
                bestPositions = []
                bestPositions.append(child.game.previousMove)
            elif(topProb == probability):
                bestPositions.append(child.game.previousMove)
            # print(str(self.currentNode.children[i].game.previousMove) + ": " + str(probability*100) +" " +str(child.visitCount))
        x = random.randrange(0, len(bestPositions))
        self.currentGame.move(bestPositions[x][0], bestPositions[x][1])
        self.follow()
        # print("played " + self.player +": " + str(self.currentGame.previousMove))
        
    def follow(self):
        if (len(self.currentNode.children) == 0 and self.currentNode.game.status == ''):
            self.nmcts.search(self.currentNode, 1) #do 1 search to expand
        for i in range(0, len(self.currentNode.children)):
            if (self.currentGame.previousMove == self.currentNode.children[i].game.previousMove):
                self.currentNode = self.currentNode.children[i]
                # print("Followed "+self.player+ ": " + str(self.currentNode.game.previousMove))
                return
        raise Exception("Cannot follow" + str(self.currentGame.previousMove) + str(self.currentNode.game.previousMove))

class RandomPlayer():
    def __init__(self, game):
        self.currentgame = game

    def chooseandPlayMove(self):
        if (self.currentgame.status != ''):
            return
        possibleMoves = self.currentgame.getValidMoves()
        x = random.randrange(0,len(possibleMoves))
        self.currentgame.move(possibleMoves[x][0], possibleMoves[x][1])

    def follow(self):
        pass