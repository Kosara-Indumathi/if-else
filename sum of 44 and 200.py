# a=44+200
# if a==123:
#     print("equal")
# else:
#     print("not equal")




n1=int(input("enter the number"))
n2=int(input("enter the number"))
n3=int(input("enter the number"))
if n1>n2 and n1>n3:           
    if n2>n3:
        print(n2,"is middle")
elif n2>n3 and n2>n1:
    if n3>n1:
        print(n3," is middle")
else:
    print(n1," is middle")
