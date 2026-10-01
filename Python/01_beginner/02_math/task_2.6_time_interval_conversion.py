"""
Write a program that converts a time interval given in minutes into hours and minutes, and prints the result in the following format:
<original number of minutes> min is <number of full hours> h <remaining number of minutes> min.
"""

num = int(input('minutes: '))
hours = num // 60
minutes = num % 60

print(f"{num} min is {hours} h {minutes} min")