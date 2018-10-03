my_sheeps = [5,7,300,90,24,50,75]

print("Hi, My name is Nhan and these are my sheep sizes: ")
print(my_sheeps)

print("Now my biggest sheep has size",max(my_sheeps),"let's shear it")

p = my_sheeps.index(max(my_sheeps))
my_sheeps[p] = 8
print("After shearing, here is my flock")
print(my_sheeps)
