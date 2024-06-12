# Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
# Sample value of n is 5
# Expected Result : 615


n = int(input())

n1 = int("%s" % n)
n2 = int("%s%s" % (n,n))


print(n2)