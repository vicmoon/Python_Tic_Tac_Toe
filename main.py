from flask import Flask, render_template, request, session, redirect, url_for
import my_secrets

app = Flask(__name__)
app.config["SECRET_KEY"] = my_secrets.SECRET_KEY 

@app.route("/")
def index():
    if "board" not in session:
        session["board"] = [""] * 9  # 3x3 board
        session["player"] = "X"

    return render_template("index.html", board=session["board"], player=session["player"])


@app.route("/move/<int:position>")
def make_move(position):
    board = session["board"]
    player = session["player"]

    if board[position] == "":  # Check if the spot is empty
        board[position] = player
        session["player"] = "O" if player == "X" else "X"  # Switch turns
        session["board"] = board

    return redirect(url_for("index"))


@app.route("/game_over")
def game_over():
    return render_template("game_over.html", winner=session.get("winner"))


@app.route('/reset')
def reset():
    session.pop('board', None)
    session.pop('player', None)
    session.pop('winner', None)

    return redirect(url_for("index"))



if __name__ == "__main__":
    app.run(debug=True)