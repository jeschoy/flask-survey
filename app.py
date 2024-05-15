from flask import Flask, render_template, flash, redirect, request
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey as survey

app = Flask(__name__)
app.config['SECRET_KEY'] = 'key'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)


responses = []

@app.route('/')
def first_page():
  return render_template('start.html', survey=survey)

@app.route('/start-survey')
def start_survey():
  responses = []
  return redirect ('/question/0')

@app.route('/question/<int:num>')
def show_question(num):
  if (responses is None):
    return redirect('/')

  if (len(responses) == len(survey.questions)):
    return render_template('/end.html')
  
  if (len(responses) != num):
    flash(f"Invalid question!")
    return redirect(f"/question/{len(responses)}")

  question = survey.questions[num]
  return render_template('question.html', question_number=num, question=question)

@app.route('/answer', methods=['POST'])
def answering_question():
  choice = request.form['answer']
  responses.append(choice)
  return redirect(f'/question/{len(responses)}')