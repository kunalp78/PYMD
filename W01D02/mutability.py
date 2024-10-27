# Immutable data types
"""
str, int, float, None, bool, complex

tuple, range
"""
# Mutable data types
"""
list, set, dict
"""
v = 3
d = 3
# print(id(v))
# print(id(d))

# print(id(v) == id(d))

t = (1, 2, 3)
t1 = (1, 2)

print(id(t) == id(t1))

l = [1, 2, 3]
l1 = [1, 2, 3]

print(id(l) == id(l1))