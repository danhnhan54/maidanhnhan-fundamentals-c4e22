import pyexcel
from collections import OrderedDict
data = [
    OrderedDict({
        'Name': 'Quan',
        'age': 19,
        'City': 'Hanoi'
    }),
    OrderedDict({
        'Name': 'Nhan',
        'age': 25,
        'City': 'Hatinh'
    }),
    OrderedDict({
        'Name': 'Nam',
        'age': 23,
        'City': 'Bacninh'
    })
]

pyexcel.save_as(records=data, dest_file_name="sample.xlsx")