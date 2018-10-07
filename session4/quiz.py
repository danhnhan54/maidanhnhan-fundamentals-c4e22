quiz = [
    "Lớp C4E22 có rất nhiều học viên.",
    "Hỏi bạn nào lớn tuổi nhất?",
    {
        1: "An",
        2: "Huy",
        3: "Cả 2 bạn",
        4: "Không đáp án nào đúng",
    },
]
print(*quiz,sep='\n')
a = int(input("Nhập đáp án của bạn vào đây: "))
if a == 2:
    print("Chính xác. Huy là người lớn tuổi nhất lớp!")
else:
    print("Rất tiếc. Đáp án đúng là 2.Huy")


