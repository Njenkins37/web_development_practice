from random import randint
from flask import Flask

app = Flask(__name__)
target = randint(0, 10)
print(target)

@app.route('/')
def home_page():
    return '<h1>Guess a number between 0 and 10 by typing it in the url.</h1>'


@app.route('/<int:guess>')
def guessed_page(guess):
    if guess < target:
        return ("<h1>Your guess is too low! Try again.</h1>")
    elif guess > target:
        return ("<h1>Your gues is too high! Try again.</h1>")
    else:
        return("<h1>You got it!</h1>")


if __name__ == '__main__':
    app.run(debug=True)
