quiz = {
    "qa":["Answer the following algebra question:","Estimate the answer (exact calculation not needed)"],
    "question":["If x = 8, then what is the value of 4(x + 3) ?","Jack score these marks in 5 math tests: 49, 81, 72, 66 and 52. What is this mean ?"],
    "choices": [[35,36, 40, 44],["About 55","About 65", "About 75", "About 85"]],
    "right choice": [4,2]
}
trueanswer = 0
for i in range (2):
    print(quiz["qa"][i])
    print(quiz["question"][i])
    for j in range (4):
        print( j+1,quiz["choices"][i][j], sep=". ")
    while True:
        answer = input("Your answer: ")
        if answer.isdigit() == False:
            print("Not found. Choose again")
        else:
            if int(answer) == quiz["right choice"][i]:
                print("Bingo")
                if int(answer) == quiz["right choice"][i]:
                    trueanswer += 1
                break
            else:
                print(':(')
                break   
print('You correctly answer',trueanswer,'out of 2 questions')