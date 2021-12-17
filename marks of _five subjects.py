# Write a python program to input marks of five subjects Physics, Chemistry, Biology, Mathematics and
# Computer. Calculate percentage and grade according to following:
# Percentage >= 90% : Grade A
# Percentage >= 80% : Grade B
# Percentage >= 70% : Grade C
# Percentage >= 60% : Grade D
# Percentage >= 40% : Grade E
# Percentage < 40% : Grade F
physics=int(input("enter the physics marks  :"))
chemistry=int(input("enter the chemistry marks :"))
biology=int(input("enter the biology marks:"))
mathematics=int(input("enter the mathematics marks:"))
computer=int(input("enter the computer marks :"))
total=physics+chemistry+biology+mathematics+computer
per=total/5
print(per)
if per>=90:
    print("grade A")
elif per>=80:
    print("grade B")
elif per>=70:
    print("grade C")
elif per>=60:
    print("grade D")
elif per>=40:
    print("grade E")
else:
    print("grade F")

