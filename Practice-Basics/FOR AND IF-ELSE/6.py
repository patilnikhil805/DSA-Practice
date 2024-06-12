# Write a Python program to convert temperatures to and from Celsius and Fahrenheit.
# [ Formula : c/5 = f-32/9 [ where c = temperature in celsius and f = temperature in fahrenheit ]
# Expected Output :
# 60°C is 140 in Fahrenheit
# # 45°F is 7 in Celsius

temp = input("input the tempreture you like to convert? eg 45F, 102C etc")

degree = int(temp[:1])

convention = temp[-1]

if convention.upper() == 'C':
    result = int(round((9 * degree ) / 5 + 32))
    