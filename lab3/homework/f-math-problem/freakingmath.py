from random import *
def eval(x,y,op):
    if op == '+':
        r = x + y
    elif op == '-':
        r = x - y
    elif op == '*':
        r = x * y
    elif op == '/':
        r = x / y
    return r

def generate_quiz():
    # Hint: Return [x, y, op, result]
    x = randint(0,10)
    y = randint(1,10)
    op = choice(['+','-','*','/'])
    error = randint(-1,1)
    result = eval(x,y,op) + error

    return [x,y,op,result]
def check_answer(x, y, op, result, user_choice):
    if result == eval(x,y,op):
        if user_choice == True:
            return True
        else:
            return False
    else:
        if user_choice == True:
            return False
        else:
            return True
