
a = str(list(input("Enter a word")))

for char in range(len(a) -1, -1, -1):
    print(a[char], end=" ")

print("\n")