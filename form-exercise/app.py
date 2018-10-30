from flask import *
app = Flask(__name__)

@app.route('/register_form',methods=['GET','POST'])
def register_form():
    if request.method == 'GET':
        return render_template('register.html')
    elif request.method == 'POST':
        form = request.form
        print(form)
        # for k,v in form.items():
        #     print(k,v,sep=": ")
        return "Thank you"

if __name__ == '__main__':
  app.run(debug=True)