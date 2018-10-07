quiz = {
    "question": "if x =8, then what is the value of 4(x+3)? ",
    "choices": [35, 36, 40, 44],
    "right choice": 4 
}
while True:
    print(quiz["question"])
    a = 1
    for i in quiz["choices"]:
        print(a,i,sep=". ")
        a += 1
    answer = input("Your answer: ")
    if answer.isdigit() == False:
        print("Not found. Choose again")
    if int(answer) == quiz["right choice"]:
        print("Bingo")
        break
    else:
        print(":(")    