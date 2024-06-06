# Write a Python program to print the alphabet pattern 'D'.
# Expected Output:

#  ****                                                                   
#  *   *                                                                  
#  *   *                                                                  
#  *   *                                                                  
#  *   *                                                                  
#  *   *                                                                  
#  **** 

result_str = ""

for row in range(0,7):
    for col in range(0,5):
        if ((col == 0 or col == 4) and (row > 0 and row < 6) or ( row == 0 or row == 6) and (col < 4)):
            result_str = result_str + "*"
        else:
            result_str = result_str + ' '
    
    result_str = result_str + "\n"

print(result_str)