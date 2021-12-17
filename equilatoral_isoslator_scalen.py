# Write a python program to check whether the triangle is equilateral, isosceles or scalene triangle.
a=int(input("enter the side:"))
b=int(input("enter the side:"))
c=int(input("enter the side:"))
if a==b==c:
    print("equilateral triangle")
elif a==b or b==c or c==a:
    print("isoslateral triangle")
else:
    print("scalene triangle")