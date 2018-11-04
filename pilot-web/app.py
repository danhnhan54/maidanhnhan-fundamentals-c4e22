from flask import Flask, render_template, request
import mlab
from poll import Poll
from random import choice

app = Flask(__name__)
mlab.connect()

@app.route('/')
def home():
    return render_template("home.html")

@app.route("/poll/<poll_code>")
def poll(poll_code):
  # 1. Get poll
  poll_list = Poll.objects(code=poll_code)
  poll = poll_list[0]
  # 2. Render
  return render_template("poll.html", p=poll)

@app.route("/polls")
def polls():
  # 1. Read All polls
  poll_list = Poll.objects()
  # for p in poll_list:
  #   print(p.question)
  # 2. Render All polls
  return render_template("polls.html", polls=poll_list)

@app.route('/new_poll',methods=["GET", "POST"])
def new_poll():
  if request.method == "GET":
    return render_template("new_poll.html")
  elif request.method == "POST":
    #1. unpack data (form)
    form = request.form
    question = form['question']
    options = []
    for k,v in form.items():
      if k != 'question':
        options.append(v)
    print(question)
    print(options)
    alphabet = "abcdefjhijklmnopqrstuvwxyz".upper()
    code = "" # short uuid python
    for _ in range(6):
      code += choice(alphabet)
    p = Poll(question=question, options=options, code=code)
    p.save()
    return "Thank you"

if __name__ == '__main__':
  app.run(debug=True)