def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number 
    return total
print(multiply(12,54,55,5,2,3,5,-7,1))