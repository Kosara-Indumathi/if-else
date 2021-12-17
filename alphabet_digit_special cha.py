char=input("enter the character")
if char>="0"and char<="9":
    print("digit")
elif (char>="a" and char<="z") or (char>="A" and char<="Z"):
    print("alphabet")
else:
    print("special character")