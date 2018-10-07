string  = input("Enter the string: ")
abc = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
for i in (abc):
    if (string.lower().count(i)) > 0:
        print(i, string.lower().count(i))