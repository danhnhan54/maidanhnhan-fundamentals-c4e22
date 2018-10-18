from calc import eval, add
# from calc import *
# import calc
x = int(input('Nhập x: '))
y = int(input('Nhập y: '))
op = input('Nhập phép tính(+,-,*,/): ')
r = eval(x,y,op)

# if op == '+':
#     r = x + y
# elif op == '-':
#     r = x - y
# elif op == '*':
#     r = x * y
# elif op == '/':
#     r = x / y
# else:
#     print("Invalid")

print(x, op, y, "=", r)