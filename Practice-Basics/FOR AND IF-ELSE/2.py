# Write a Python program that accepts a sequence of comma-separated numbers from the user and generates a list and a tuple of those numbers.
# Sample data : 3, 5, 7, 23
# Output :
# List : ['3', ' 5', ' 7', ' 23']
# Tuple : ('3', ' 5', ' 7', ' 23')


# user = list(input("Enter Numbers"))
# tuple = user
# print(user)
# print(tuple)

values = input("Enter number seperated with commas")

list = values.split()

tuple = tuple(list)

print(list)

print(tuple)