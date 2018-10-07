person = {
    "name": "Nhan",
    "age": 23,
    "location": "Hanoi",
    "status": "Single",
}
# for k in person.keys():
#     print(person[k])

# for v in person.values():
#     print(v)

for k,v in person.items():
    print(k,v,sep=": ")