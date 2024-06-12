# Write a Python program to calculate the sum of a list of numbers using recursion.

def sum(numbers):
    if len(numbers) == 1:
        return numbers[0]
    else:
        return numbers[0] + sum(numbers[1:])
    
print(sum([1,2,3,4,5]))