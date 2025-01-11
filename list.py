# to_do = ["study", "eat", "sleep", "repeat"]
# print(to_do)
# numbers = [1, 2, 3, 4, "cinco", True, 6.7]
# print(type(numbers))
# print(len(numbers))

# numbers.append(False)
# print(numbers)
# print(numbers.index(3))

# del numbers[-2]
# print(numbers)

a = [1, 2, 3, 4, 5]
b = a 
del a[0]
print(a)
print(b)
c = a[:]
print(id(a))
print(id(b))
print(id(c)) 
a.append(6)
print(a)
print(b)
print(c)

