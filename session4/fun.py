person = {
    "name": "Nhan",
    "age": 23,
    "location": "Hanoi",
    "status": "Single",
}

print(person)

while True:
    a = input("What do you want (D/U)? ")

    if a == "D":
        while True:
            b = input("What info do you want to delete? ")
            if b in person:
                del person[b]
                print(person)
                break
            else:
                print("Wrong key. Try again!")
        break
    elif a == "U":
        k = input("What key? ")
        v = input("What value? ")
        person[k] = v
        print(person)
        break
    else:
        print("Wrong! Try again!")