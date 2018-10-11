from matplotlib import pyplot

machine_type = [18, 4, 2]
machine_name = ['PC', 'Mac','Linux']
pyplot.pie(machine_type, labels = machine_name,autopct="%.1f%%",explode=[0, 0.05, 0.05])
pyplot.axis("equal")
pyplot.title("Ty le hdh trong lop")
pyplot.show()
