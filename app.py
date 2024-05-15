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
  """To render the introduction page"""
  return render_template('start.html', survey=survey)

@app.route('/start-survey')
def start_survey():
  """Clear the responses and start a new survey"""

  #To clear the responses
  responses = []

  return redirect ('/question/0')

@app.route('/question/<int:num>')
def show_question(num):
  """To display the current question"""

  #To redirect if there are no responses yet
  if (responses is None):
    return redirect('/')

  #To redirect to the end if the survey has been completed
  if (len(responses) == len(survey.questions)):
    return render_template('/end.html')
  
  #To redirect if user tries to visit invalid page
  if (len(responses) != num):
    flash(f"Invalid question!")
    return redirect(f"/question/{len(responses)}")

  #To select the current question and render on page
  question = survey.questions[num]

  return render_template('question.html', question_number=num, question=question)

@app.route('/answer', methods=['POST'])
def answering_question():
  """To log answers and add to the responses"""

  #To grab the answer
  choice = request.form['answer']
  
  #To add to the responses list
  responses.append(choice)

  #To move on to the next question
  return redirect(f'/question/{len(responses)}')