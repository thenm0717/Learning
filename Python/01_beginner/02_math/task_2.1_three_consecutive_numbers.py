"""
Write a program that prints three consecutive numbers, each on a separate line.
The first number is entered by the user; the program must calculate the remaining numbers itself.
"""

num_1 = int(input())
num_2 = num_1 + 1
num_3 = num_2 + 1

print(num_1, num_2, num_3, sep='\n')
