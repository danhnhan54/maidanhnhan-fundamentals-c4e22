from flask import *
import mlab
from poll import Poll
from random import choice
from vote import Vote

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

@app.route("/vote/<poll_code>",methods=["GET", "POST"])
def vote(poll_code):
  #1. Get poll
  poll = Poll.objects(code=poll_code).first()

  #2. Render poll detail + form
  if request.method == "GET":
    return render_template("vote_selection.html",p=poll)

  #3. Handle form request(POST)

  # Nếu để input là điền số:
  # elif request.method == "POST":
  #   form = request.form
  #   name = form['user_name']
  #   number = int(form['number'])
  #   option = poll['options'][number-1]
  #   return render_template("vote2.html",name=name, option=option)
  
  elif request.method == "POST":
    form = request.form
    choice = form['choice']
    name = form['user_name']
  # 4. Save
    new_vote = Vote(choice=choice, voter=name, poll=poll)
    new_vote.save()
    return "Voted"


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
    url = url_for("poll",poll_code=p.code)
    return redirect(url)

if __name__ == '__main__':
  app.run(debug=True)