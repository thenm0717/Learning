"""
Write a program that checks that for a given four-digit number the following condition is satisfied: the sum of the first and 
last digits equals the difference of the second and third digits.
"""

num = int(input('Enter num: '))

if 1000 >= num <= 9999:
    first = num // 1000
    second = (num % 1000) // 100
    third = (num % 100) // 10
    fourth = num % 10

    if first + fourth == second - third:
        print('True')
    else:
        print('False')

else:
    print('To run the program, you need to enter a four-digit number.')