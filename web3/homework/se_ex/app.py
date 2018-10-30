from flask import *
app = Flask(__name__)

@app.route('/new_bike',methods=['GET','POST'])
def new_bike():
    if request.method == 'GET':
        return render_template('new_bike.html')
    elif request.method == 'POST':
        form = request.form
        for k,v in form.items():
            print(k,v,sep=": ")
        return "Thank you"
        

if __name__ == '__main__':
  app.run(debug=True)