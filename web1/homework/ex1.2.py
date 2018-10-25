from flask import *
app = Flask(__name__)

@app.route("/bmi/<int:weight>/<int:height>")
def bmi(weight,height):
    bmi = weight/(height*height/10000)
    if bmi < 16:
      result = "Severely underweight"
    elif 16<= bmi <18.5:
      result = "Underweight"  
    elif 18.5 <= bmi < 25:
      result = "Normal"
    elif 25 <= bmi < 30:
      result = "Overweight"  
    else:
      result = "Obese"
    bmi = str(bmi)
    return render_template("ex_bmi.html",bmi = bmi,result = result)

if __name__ == '__main__':
  app.run(debug=True)