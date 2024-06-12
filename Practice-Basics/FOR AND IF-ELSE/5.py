# Write a Python program to find those numbers which are divisible by 7 and multiples of 5, between 1500 and 2700 (both included).

n1 = []

for a in range (1500,2701):
    if (a % 7 == 0 and a % 5 == 0): 
        n1.append(str(a))

print(n1)