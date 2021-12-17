# Take two user inputs one as day and one as meal time. Show the following
# table using nested if statements :
# 1. Day = Monday
# Breakfast = Poori Sabzi
# Lunch = Sambhar Rice
# Dinner = Chicken Rice
# 2. Day = Tuesday
# ◦ Breakfast = Poha
# ◦ Lunch = Rajma Rice
# ◦ Dinner = Roti Sabzi.




day=input("enter the day:-")
meal_time=input("enter the meal time:-")
if day=="monday":
    if meal_time=="breakfast":
        print("poori sabji")
    if meal_time=="lunch":
        print("sambar rice")
    if meal_time=="dinner":
            print("chicken rice")
elif day=="tuesday":
    if meal_time=="breakfast":
            print("poha")
    if meal_time=="lunch":
            print("rajma chaval")
    if meal_time=="dinner":
                print("roti sabji")
