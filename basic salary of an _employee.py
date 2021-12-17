# Write a python program to input basic salary of an employee and calculate its Gross salary according to
# following:
# Basic Salary <= 10000 : HRA = 20%, DA = 80%
# Basic Salary <= 20000 : HRA = 25%, DA = 90%
# Basic Salary > 20000 : HRA = 30%, DA = 95%
basic_salary=int(input("enter the salary"))
if basic_salary<=10000:
 print("gross salary",basic_salary+basic_salary*20/100+basic_salary*80/100)
elif basic_salary>10000 and basic_salary<=20000:
    print("gross salary",basic_salary+basic_salary*25/100+basic_salary*90/100)
else:
    print("gross salary",basic_salary+basic_salary*30/100+basic_salary*95/100)









