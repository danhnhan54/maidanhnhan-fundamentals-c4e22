from random import randint
x = randint(0,10)
y = randint(1,10)
error = randint(-1,1)
a = randint(0,3) 
op_list = ['+','-','*','/']
s_list =[x + y + error,x - y + error, x * y + error, x / y + error]
op = op_list[a]
s = s_list[a]

print('{0} {1} {2} = {3}'.format(x,op,y,s))
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