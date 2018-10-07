person = {
    "name": "Quan",
    "age": 22,
    "location": "Hanoi",
}
# Trả lời cơ bản:
# a = input("Enter a key to check: ")
# print(person[a])

# Dùng try except

# Dùng if, câu lệnh "in"/"not in": "a in person"/ "a not in person"
while True:
    a = input("Enter a key to check: ")
    if a in person:
        print(person[a])
        break
    else:
        print("Wrong key. Try agian!")