# Write a python program to calculate profit or loss.
cp=int(input("enter the cost price"))
sp=int(input("enter the selling  price"))
if (sp-cp)>0:
    print(sp-cp,"profit")
elif (sp-cp)<0:
    print(cp-sp,"loss")
else:
    print("no profit,no loss")