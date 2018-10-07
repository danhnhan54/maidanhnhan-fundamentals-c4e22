prices = {
    "banana":4,
    "apple":2,
    "orange":1.5,
    "pear":3
}
stock = {
    "banana": 6,
    "apple":0,
    "orange":32,
    "pear":15
}

for i in prices:
    print(i)
    print("price:", prices[i])
    print("stock:", stock[i],"\n")

total = 0
for i in prices:
    money = prices[i]*stock[i]
    print(i,money,sep=": ")
    total += money
print("Number of money if I sold all my food is:", total)