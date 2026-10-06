"""
When registering on websites, you are required to enter your password twice. This is done for security reasons, as this approach 
reduces the chance of entering the password incorrectly.
Write a program that compares a password and its confirmation. If they match, the program should output the text "Password accepted"
(without quotes); otherwise, it should output "Password not accepted" (without quotes).
"""

new_pass = input('Enter new pass: ')
confirm_pass = input('Enter confirm pass: ')

if new_pass == confirm_pass:
    print('Password accepted')
else:
    print('Password not accepted')