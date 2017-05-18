from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route('/six')
def dice_roll():
    a = str(random.randint(1,6))
    return render_template('layout.html', die_type = "six-sided", 
            num = a)

@app.route('/eight')
def eight_roll():
    a = str(random.randint(1,8))
    return render_template('layout.html', die_type = "eight-sided", 
            num = a)

@app.route('/ten')
def ten_roll():
    a = str(random.randint(1, 10))
    return render_template('layout.html', die_type = "ten-sided",
            num = a)

@app.route('/twelve')
def twelve_roll():
    a = str(random.randint(1,12))
    return render_template('layout.html', die_type = 'twelve-sided',
            num = a)

@app.route('/twenty')
def twenty_roll():
    a = str(random.randint(1,12))
    return render_template('layout.html', die_type = 'twenty-sided',
            num = a)
