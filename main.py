from flask import Flask
from random import randint

number = randint(0,10)

app = Flask(__name__)

@app.route('/')
def start():
    return "<h1>Guess a number between 0 and 9</h1>"\
           "<img src='https://media.giphy.com/media/2lQCCSp19EDAy5d7c7/giphy.gif?cid=ecf05e47zxr2tx78afl2klmqxwe6g70279ojvao26mhk6rk5&ep=v1_gifs_search&rid=giphy.gif&ct=g' width=500>"

@app.route('/<int:guess>')
def check(guess):
    if guess > number:
        return "<h1 style='color: purple'>Too High</h1>"\
               "<img src='https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExZHdqYWYxNGh5cjByam83ODF1ZHp5NWh1ZHMyNnowMDJ4OHc3dGJlcSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/oFVr84BOpjyiA/giphy.gif' width=500>"
    
    elif guess < number:
        return "<h1 style='color: red'>Too Low</h1>"\
                "<img src='https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExZHdqYWYxNGh5cjByam83ODF1ZHp5NWh1ZHMyNnowMDJ4OHc3dGJlcSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/oFVr84BOpjyiA/giphy.gif' width=500>"
    else:
        return "<h1 style='color: green'>Correct</h1>"\
                "<img src='https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExZHdqYWYxNGh5cjByam83ODF1ZHp5NWh1ZHMyNnowMDJ4OHc3dGJlcSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/eKNrUbDJuFuaQ1A37p/giphy.gif' width=500>"

if __name__ == '__main__':
    app.run(debug=False)
