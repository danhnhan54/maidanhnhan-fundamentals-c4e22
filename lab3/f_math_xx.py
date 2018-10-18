from random import randint,choice
from calc import eval

def generate_quiz():
    x = randint(0,10)
    y = randint(1,10)
    op = choice(['+','-','*','/'])
    error = randint(-1,1)
    r = eval(x,y,op) + error

    return [x,y,op,r]

x, y, op, r = generate_quiz()

output = '{0} {1} {2} = {3}'.format(x,op,y,r)
print(output)
inp = input('Y/N: ').upper()
if error == 0:
    if inp == 'Y':
        print('Yay')
    elif inp == 'N':
        print('Nah')
    else:
        print('Wrong input')
else:
    if inp == 'Y':
        print('Nah')
    elif inp == 'N':
        print('Yay')
    else:
        print('Wrong input')