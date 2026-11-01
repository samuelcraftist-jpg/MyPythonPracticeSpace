"""
Area of,
rectagle : length * breadth 

square: side * side (or side ^2 ig)

Circle: PI * radius ^ 2 (PI = 3.14159... ig i forgot if its wrong) imma use math library so,
 i can use pi value with much better accuracy

Triangle: 0.5 * base * height
"""

import math

print("1. Rectangle")
print("2. Square")
print("3. Circle")
print("4. Triangle")


import math

print("1. Rectangle")
print("2. Square")
print("3. Circle")
print("4. Triangle")

try:
    choice = int(input("Enter choice: "))

    if choice == 1:
        l = float(input("Enter length: "))
        b = float(input("Enter breadth: "))
        area = l * b

    elif choice == 2:
        s = float(input("Enter side: "))
        area = s * s

    elif choice == 3:
        r = float(input("Enter radius: "))
        area = math.pi * r * r

    elif choice == 4:
        b = float(input("Enter base: "))
        h = float(input("Enter height: "))
        area = 0.5 * b * h

    else:
        area = None
        print("Invalid choice")

    if area is not None:
        print("Area:", area)

except ValueError:
    print("Enter a valid input!")