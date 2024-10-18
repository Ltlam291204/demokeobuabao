from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/play', methods=['POST'])
def play():
    choices = ["Keo", "Bua", "Bao"]
    user_choice = int(request.form['choice'])
    comp_choice = random.randint(0, 2)

    user_choice_name = choices[user_choice]
    comp_choice_name = choices[comp_choice]

    if user_choice == comp_choice:
        result = "HOA"
    elif (user_choice == 0 and comp_choice == 1) or (comp_choice == 0 and user_choice == 1):
        result = 'Bua'
    elif (user_choice == 0 and comp_choice == 2) or (comp_choice == 0 and user_choice == 2):
        result = 'Keo'
    else:
        result = 'Bao'

    if result == "HOA":
        winner = "Hoa roi!"
    elif result == user_choice_name:
        winner = "Nguoi choi thang!"
    else:
        winner = "May tinh thang!"

    return render_template('index.html', user_choice=user_choice_name, comp_choice=comp_choice_name, winner=winner)

if __name__ == '__main__':
    app.run(debug=True)
