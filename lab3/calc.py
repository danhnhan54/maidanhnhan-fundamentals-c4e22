def add(x,y):
    r = x + y
    return r

# def eval(x,y,op):
#     if op == '+':
#         r = x + y
#     elif op == '-':
#         r = x - y
#     elif op == '*':
#         r = x * y
#     elif op == '/':
#         r = x / y
#     return r

def eval(x,y,op):
    if op == '+':
        return x + y
    elif op == '-':
        return x - y
    elif op == '*':
        return x * y
    elif op == '/':
        return x / y

# a = int(input('a= '))
# b = int(input('b= '))
# t = add(a,b)
# print(t)