"""
Write a program that finds the digits of a four-digit number.
"""

num = int(input())

thousands = num // 1000
hundreds = (num % 1000) // 100
tens = (num % 100) // 10
units = num % 10

print(f"thousands = {thousands},hundreds = {hundreds}, tens = {tens}, units = {units},")