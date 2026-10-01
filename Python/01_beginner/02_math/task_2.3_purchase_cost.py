"""
Write a program that calculates the total cost of three computers, each consisting of a monitor, a system unit, a keyboard, 
and a mouse.

Input format:
The program receives four integers (each on a separate line): the cost of the monitor, the cost of the system unit, 
the cost of the keyboard, and the cost of the mouse.
"""

monitor = int(input('monitor_price: '))
system_unit = int(input('system_unit_price: '))
keyboard = int(input('keyboard_price: '))
mouse = int(input('mouse_price: '))

res = 3 * (monitor + system_unit + keyboard + mouse)
print(res)