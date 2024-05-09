from flask import Flask, render_template, flash
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey

app = Flask(__name__)
app.config['SECRET_KEY'] = 'key'
debug = DebugToolbarExtension(app)

responses = []

@app.route('/')
def first_page():
  return render_template('start.html', survey=satisfaction_survey)