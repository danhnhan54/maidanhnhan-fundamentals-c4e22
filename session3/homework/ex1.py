items = ["T-Shirt","Sweater"]

a = input("Welcome to our shop, what do you want (C, R, U, D)?  ")

if a == "R":
    print("Our items: ",end="")
    print(*items,sep=", ")
elif a == "C":
    items.append(input("Enter new item: "))
    print("Our items: ",end="")
    print(*items,sep=", ")
elif a == "U":
    while True:
        p = int(input("Update position? "))
        if p > len(items):
            print("Wrong position. Please try new one")
        else:
            items[p-1] = input("New item? ")
            print("Our items: ",end="")
            print(*items,sep=", ")
            break
elif a == "D":
    while True:
        p = int(input("Delete position? "))
        if p > len(items):
            print("Wrong position. Please try new one")
        else:
            items.pop(p-1)
            print("Our items: ",end="")
            print(*items,sep=", ")
            break