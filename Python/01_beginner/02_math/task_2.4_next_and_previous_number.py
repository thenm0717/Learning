"""
Write a program that reads an integer and prints the next and previous integers in the following format:

The next number after <current number>: <next number>
The previous number before <current number>: <previous number>
"""

num = int(input())

print(f"The next number after {num}: {num + 1}")
print(f"The previous number before {num}: {num - 1}")