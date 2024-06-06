# Write a Python program that takes two digits m (row) and n (column) as input and generates a two-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.
# Note :
# i = 0,1.., m-1
# j = 0,1, n-1.

# Test Data : Rows = 3, Columns = 4
# Expected Result : [[0, 0, 0, 0], [0, 1, 2, 3], [0, 2, 4, 6]]

m = int(input("Enter the Number of Rows"))
n = int(input("Enter the Number of Columns"))

D_array = [[0 for col in range(n)] for row in range(m)]

for row in range(m):
    for col in range(n):
        D_array[row][col] = row * col

print(D_array)
    