while True:
    pwd = input("Enter your password: ")
    if len(pwd) >= 8:
        if not pwd.isdigit():
            print("Ok")
            break
        else:
            print("Must contain at least an alphabet character")
    else:
        print("Not long enough")