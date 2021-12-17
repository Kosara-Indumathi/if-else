n1=int(input("enter the number"))
n2=int(input("enter the number"))
n3=int(input("enter the number"))
if n1>n2 and n1>n3:
    if n2>n3:
        print(n2,"is second maximum")
    else:
        print(n3,"is less")
elif n2>n3 and n2>n1:
    if n3>n1:
        print(n3,"is second maximum")
    else:
        print(n1,"is less")
else:
    if n3>n1 and n3>n2:
        print(n1,"is second maximum")
    else:
        print(n2,"is less")