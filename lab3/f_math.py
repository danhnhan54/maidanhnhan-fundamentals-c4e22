from random import randint
x = randint(0,10)
y = randint(1,10)
s = randint(x+y-1,x+y+1)
print('{0} + {1} = {2}'.format(x,y,s))
inp = input('Y/N: ').upper()
if s==x+y:
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
