from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def game():
    result = ""
    computer_choice = ""
    
    if request.method == "POST":
        user_choice = request.form.get("choice")
        choices = ["rock", "paper", "scissors"]
        computer_choice = random.choice(choices)

        if user_choice == computer_choice:
            result = "It's a Tie!"
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            result = "You Win!"
        else:
            result = "You Lose!"
    
    return render_template("index.html", result=result, computer_choice=computer_choice)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

