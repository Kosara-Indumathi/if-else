balance=10000
language=input("enter the language")
language="english","hindhi","telugu"
print("welcome to our bank world")
pin_code=input("enter the four digit number")
user_choose=("balance enquiry","withdraw","deposit","closing")
if pin_code=="9441":
    print("balance enquiry")
    print("withdraw")
    print("deposit")
    print("closing")
    user_choose=input("enter choose")
    if user_choose=="balance enquiry":
        if balance>0:
           print(balance)
        else:
            print("nothing")
    elif user_choose=="withdraw":
        withdraw=int(input("enter the amount"))
        if balance>withdraw:
            print("sucess your amount is now:",balance-withdraw)
        else:
            print("insuffiecient balance")
    elif user_choose=="deposit":
        deposit=int(input("enter deposit amount"))
        if balance>0:
            total_amount=balance+deposit
            print(total_amount)
        else:
            print("something wrong")
    elif user_choose=="closing":
        print("closing")
else:
    print("sorry wrong pass word try again")


