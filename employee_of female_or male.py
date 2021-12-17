# Ask user to enter age, sex ( M or F ), marital status ( Y or N ) and then using
# following rules print their place of service.
# if employee is female, then she will work only in urban areas.
# if employee is a male and age is in between 20 to 40 then he may work in
# anywhere
# if employee is male and age is in between 40 t0 60 then he will work in urban areas
# only.
# And any other input of age should print "ERROR".
 

sex=input("enter the sex")
age=int(input("enter the age"))
if sex=="m":
    if age>=20 and age<=40:
     print("he will work in any areas")
    else:
        print("no")
elif sex=="m":
    if age>=40 and age<=60:
        print("he will work in urban areas only")
    else:
        print("nothing")
else:
    if sex=="f":
        print("she only work urban area")
    else:
        print("error")
