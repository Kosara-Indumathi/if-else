num=int(input("enter the number"))
if (num%4==0):
    if(num%100==0):
        if(num%400==0):
            print("is a leap year")
        else:
            print("not leap year")
    else:
        print("leap year")
else:
    print("not a leap year")
