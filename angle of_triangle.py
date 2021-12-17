# write a program to input angles of a triangle and check whether triangle is valid or not.
a=(input("enter the angle"))
b=(input("enter the angle"))
c=(input("enter the angle"))
if a+b>c and b+c>a and c+a>b:
    print("triangle")
else:
    print("not a triangle")