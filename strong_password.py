password=input("enter the password")
if len(password)>=8 and len(password)<=16:
    if "special characters" in password or "@" in password or "#" in password:
        if "A" or "z" in password:
           if "0" or "9" in password:
               print("strong password")
           else:
               print("week password")
        else:
            print("weekly password")
    else:
        print("nothing")
else:
    print("wrong password")