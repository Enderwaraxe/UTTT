from re import L
from flask import Flask, request, render_template
from ultimatetictactoe import *
import copy
import time
app = Flask(__name__)
uttt = UltimateTicTacToe()
mcts = MCTS()
Bot = None
def displayBoard(isbotmove):
    print("displayed")
    x = uttt.getboard()
    allstatus = [0]*9
    validmoves = uttt.getValidMoves()
    bigboardtemp = [0]*9
    for i in range(0, 9):
        bigboardtemp[i] = copy.deepcopy(x[i].board)
        allstatus[i] = copy.deepcopy(x[i].status)
    if (not isbotmove):
        for i in range(0, len(bigboardtemp)):
            for j in range(0, 9):
                if ((i+1,j+1) in validmoves):
                    bigboardtemp[i][j] = 3
    return render_template('template.html',bigboard = bigboardtemp, bigstat= uttt.status, allstatus = allstatus)

@app.route("/")
def create():
    print("created")
    global uttt,mcts, Bot
    uttt = UltimateTicTacToe()
    # Bot = RandomPlayer(uttt)
    Bot = MCTSBotPlayer(uttt, mcts)
    return displayBoard(False)

@app.route("/play")
def play():
    print("played")
    big = request.args.get('bigpos')
    small = request.args.get('smallpos')
    uttt.bigmove(int(big)+1, int(small)+1)
    return displayBoard(True)

@app.route("/botplay")
def botplay():
    # time.sleep(0.5)
    Bot.chooseandPlayMove()
    return displayBoard(False)