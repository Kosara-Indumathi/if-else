# beds=int(input("enter the bed"))
# girls=int(input("enter the girls"))
# if beds>=girls:
#     print(beds-girls,"girls are left")
# else:
#     print(girls-beds,"beds are left")





beds=int(input("enter the beds"))
girls=int(input("enter the girls"))
if girls>beds:
    print("girls go to another room")
    if beds>girls:
        print("beds go to another room")
    if beds==girls:
        print("both are equal")
else:
    print("no need of anything")
    