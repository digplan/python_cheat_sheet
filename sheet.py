# Comment
""" 
    Multi line comment
"""
a = 1
print(a)
A = 2
print(a, A)
A = 3
print(A)

b, c = 9, 5
print(b / c) # 1.8
print(b // c) # 1

name = 'CB'
print(f"This is a name {name} of length {len(name)}")

# LIST
d = [1, 2, 3, 'four']
a = [None] * 3

a, b, c, e = d
d.sort()

for i, v in enumerate(range(3)):
    print(i, v)

e = list()
print(d)
print(type(d)) # <class 'list'>
print(d[2:4])  # [3, 'four']
print(d[2:])   # [3, 'four']
print(d[:3])   # [1, 2, 3]
print(d[2:2:1]) #?

# List Comprehension
[(lambda x: x**2)(i) for i in range(10)]
[x**2 if x > 5 else 0 for x in range(10)]

e = d[:] # Deep copy
print(f"New copy {e}")
# remove, insert, extend, in, len
# Tuple immutable, unpack
#

f = {'one': 'two', 'key': 'val'}
g = dict()
print(f)
print(type(f)) # <class 'dict'>
# h = input('Enter some data: ')

# keys, values, get update
# set

# Ternary
print("Yes" if True == True else "No")

# iterate lists, enumerate

# file, json
# fir line in file

# functions

# classes, modules, decorators, generators, 

# System
import sys, os
print(f"Arguments: {sys.argv}")
# print(f"Arguments: {os.environ}")

if __name__ == '__main__':
    print("myfile")

# Time & Date
import time
time.time()
from datetime import date, datetime
date.today()
datetime.utcnow().isoformat()