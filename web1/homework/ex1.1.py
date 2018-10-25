from flask import *
app = Flask(__name__)

@app.route("/bmi/<int:weight>/<int:height>")
def bmi(weight,height):
    bmi = weight/(height*height/10000)
    if bmi < 16:
      return "BMI = " + str(bmi) + " You are Severely underweight"
    elif 16<= bmi <18.5:
      return "BMI = " + str(bmi) + " You are Underweight"  
    elif 18.5 <= bmi < 25:
      return "BMI = " + str(bmi) + " You are Normal"
    elif 25 <= bmi < 30:
      return "BMI = " + str(bmi) + " You are Overweight"  
    else:
      return "BMI = " + str(bmi) + " You are Obese"  

if __name__ == '__main__':
  app.run(debug=True)