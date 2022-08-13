from ultimatetictactoe import *
from NeuralMonteCarloTreeSearch import *
from policy_value_network import PolicyValueNetwork
from BotPlayer import NMCTSBotPlayer, RandomPlayer
import torch.nn as nn
import time
def loadPolicyValueNet(weightFilePath, device) -> nn.Module:
    policyValueNet = PolicyValueNetwork()
    policyValueNet.to(torch.device(device))
    stateDict = torch.load(weightFilePath, map_location=torch.device(device))
    policyValueNet.load_state_dict(stateDict)
    policyValueNet.eval()
    return policyValueNet

def playGame():
    ultimateGame = UltimateTicTacToe()
    time0 = time.time()
    policyNet = loadPolicyValueNet("C:/Users/Joshua Ni/Downloads/policy_value_net_100000.pt",'cuda')
    isOsTurn = False
    time1 = time.time()
    for i in range(0, 10):
        BotXPlayer = NMCTSBotPlayer(ultimateGame, policyNet, 20)
        # BotOPlayer = RandomPlayer(ultimateGame)
        BotOPlayer = NMCTSBotPlayer(ultimateGame, policyNet, 10)
        while(ultimateGame.status == ''):
            print("\033c", end = '')
            ultimateGame.printBoard()
            if (isOsTurn):
                BotOPlayer.move()
            else:
                BotXPlayer.move()
            isOsTurn = not isOsTurn
        if (ultimateGame.status == 'x'):
            # print("X Wins!")
            ultimateGame.xWins+=1
        elif (ultimateGame.status == 'o'):
            # print("O Wins!")
            ultimateGame.oWins+=1
        elif (ultimateGame.status == 't'):
            # print("Tie!")
            ultimateGame.ties+=1
        isOsTurn = False
        ultimateGame.reset()
    time2 = time.time()
    print("loading time: " +str(time1-time0))
    print("time taken: " + str(time2-time1))
        
    print(str(ultimateGame.xWins) + " " + str(ultimateGame.oWins) + " " + str(ultimateGame.ties))

if __name__ == "__main__":
    playGame()