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

d = [1, 2, 3, 'four']
e = list()
print(d)
print(type(d)) # <class 'list'>
print(d[2:4])  # [3, 'four']
print(d[2:])   # [3, 'four']
print(d[:3])   # [1, 2, 3]
print(d[2:2:1]) #?

e = d[:] # Deep copy
print(f"New copy {e}")
# remove, insert, extend, in, len
# Tuple immutable, unpack


f = {'one': 'two', 'key': 'val'}
g = dict()
print(f)
print(type(f)) # <class 'dict'>
h = input('Enter some data: ')
print(h)
# keys, values, get update
# set

# Ternary
print("Yes" if True == True else "No")

# iterate lists, enumerate
# file, json
# functions
# classes, modules, decorators, generators, 