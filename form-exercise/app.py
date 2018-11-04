from flask import *
import mlab
from register import Register
from random import choice
app = Flask(__name__)
mlab.connect()

@app.route('/register_form',methods=['GET','POST'])
def register_form():
    if request.method == 'GET':
        return render_template('register.html')
    elif request.method == 'POST':
        form = request.form
        info = {}
        print(form)
        for k,v in form.items():
            info[k] = v
        r = Register(info=info)
        r.save()
        return "Thank you"

if __name__ == '__main__':
  app.run(debug=True)