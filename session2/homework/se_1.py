W = int(input("Your weight(kg): "))
H = int(input("Your height(cm): "))
BMI = W/(H*H/10000)
print("BMI=",BMI)

if BMI < 16:
    print("Severely underweight")
elif BMI < 18.5:
    print("Underweight")
elif BMI < 25:
    print("Normal")
elif BMI < 30:
    print("Overweight")
else:
    print("Obese")