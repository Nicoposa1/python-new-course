to_do = ["study", "eat", "sleep", "repeat"]
print(to_do)
numbers = [1, 2, 3, 4, "cinco", True, 6.7]
print(type(numbers))
print(len(numbers))

numbers.append(False)
print(numbers)
print(numbers.index(3))

del numbers[-2]
print(numbers)