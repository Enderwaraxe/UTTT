from flask import Flask, request, render_template
from ultimatetictactoe import UltimateTicTacToe
import copy
import time
from BotPlayer import NMCTSBotPlayer, RandomPlayer
from nmctsvsrandom import loadPolicyValueNet
import argparse

app = Flask(__name__)
policyNet = None
context = {}
device = "cpu"
policyFilePath = "policy_value_net_100000.pt"
class Game:
    def __init__(self) -> None:
        self.uttt = UltimateTicTacToe()
        self.botX= None
        self.botO = None
        self.xPlayer = None
        self.oPlayer = None
        self.isOTurn = False
        self.creationTime = time.time()

def cleanup():
    global context
    newContext = {}
    currentTime = time.time()
    for user in context:
        if(currentTime - context[user].creationTime < 3600):
            newContext[user] = context[user]
    context = newContext

def displayBoard(isHumanNext, game):
    print("displayed")
    x = game.uttt.getBoard()
    allStatus = [0]*9
    validMoves = game.uttt.getValidMoves()
    tempBigBoard = [0]*9
    for i in range(0, 9):
        tempBigBoard[i] = copy.deepcopy(x[i].board)
        allStatus[i] = copy.deepcopy(x[i].status)
    if (isHumanNext):
        for i in range(0, len(tempBigBoard)):
            for j in range(0, 9):
                if ((i+1,j+1) in validMoves):
                    tempBigBoard[i][j] = 3
    return render_template('uttt.html',bigBoard = tempBigBoard, bigStat= game.uttt.status, allStatus = allStatus)

@app.route("/start")
def start():
    print("created")
    global context, device
    user = request.headers.get('User-Agent')
    game = context[user]
    game.isOTurn = False
    game.xPlayer = request.args.get('xplayer')
    game.oPlayer = request.args.get('oplayer')
    game.uttt = UltimateTicTacToe()

    if (game.xPlayer == "TortiseBot"):
        game.botX = NMCTSBotPlayer(game.uttt, policyNet, 1000, device)
    elif(game.xPlayer == "HareBot"):
        game.botX = NMCTSBotPlayer(game.uttt, policyNet, 1, device)
    else:
        game.botX = None
    if (game.oPlayer == "TortiseBot"):
        game.botO = NMCTSBotPlayer(game.uttt, policyNet, 1000, device)
    elif(game.oPlayer == "HareBot"):
        game.botO = NMCTSBotPlayer(game.uttt, policyNet, 1, device)
    else:
        game.botO = None
    context
    if (game.xPlayer == "Human"):
        return displayBoard(True, game)
    else:
        return botplay()

@app.route("/")
def root():
    global context, policyFilePath, device, policyNet
    cleanup()
    policyNet = loadPolicyValueNet(policyFilePath, device)
    user = request.headers.get('User-Agent')
    game = Game()
    context[user] = game
    print("loading policy from: " + policyFilePath + ", " + device)
    return displayBoard(False, game)

@app.route("/play")
def play():
    global context
    user = request.headers.get('User-Agent')
    game = context[user]
    print("played")
    big = request.args.get('bigpos')
    small = request.args.get('smallpos')
    game.uttt.move(int(big)+1, int(small)+1)
    game.isOTurn = not game.isOTurn
    if (game.xPlayer != "Human" or game.oPlayer!="Human"):
        return displayBoard(False, game)
    else:
        return displayBoard(True, game)

@app.route("/botplay")
def botplay():
    global context
    user = request.headers.get('User-Agent')
    game = context[user]
    if (game.uttt.status != ""):
        return
    if (game.isOTurn):
        if (game.oPlayer == "HareBot"):
            time.sleep(0.25)
        game.botO.move()
    else:
        if (game.xPlayer == "HareBot"):
            time.sleep(0.25)
        game.botX.move()
    game.isOTurn = not game.isOTurn
    if(game.xPlayer != "Human" and game.oPlayer!="Human"):
        return displayBoard(False, game)
    else:
        return displayBoard(True, game)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8888)