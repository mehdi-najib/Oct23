numbers = [1, 1, 2, 3, 4]

unique = set(numbers)

second = {1, 5}
second.add(4)

print(second)
print(unique)
second.remove(5)
print(len(second))