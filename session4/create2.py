person = {
    "name": "Quan",
    "age": 22,
}
print(person)
# k = input("Enter key: ")
# v = input("Enter value: ")
text = input("Enter new info: ")
pair = text.split(",")
# key = pair[0]
# value = pair[1]
# Cach viet khac:

key, value = pair

person[key]= value


print(person)