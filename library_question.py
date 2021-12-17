# Your local library needs your help! Given the expected and actual return dates
# for a library book, create a program that calculates the fine (if any). The fee
# structure is as follows:
# 1.
# If the book is returned on or before the expected return date, no fine will
# be charged (i.e.: fine = 0).
# 2.
# If the book is returned after the expected return. but still within the same
# calendar month and year as the expected return date, fine = Rs.15 * number of
# days late.
# 3.
# If the book is returned after the expected return month but still within the
# same calendar year as the expected return date, the fine = Rs.500 * number of
# days late.
# 4.
# If the book is returned after the calendar year in which it was expected,
# there is a fixed fine of Rs.10,000.


expected_date=int(input("enter the expected date:-"))
expected_month=int(input("enter the expected month:-"))
expected_year=int(input("enter the expected year:-"))
return_date=int(input("enter the return date:-"))
return_month=int(input("enter the return month:-"))
return_year=int(input("enter the return year:-"))
if expected_date>=return_date:
    print("no fine will be charged") 
if expected_date<=return_date:
    if expected_month==return_month:
        if expected_year==return_year:
            print((return_date-expected_date)*15,"is your fine:-")
if return_date>expected_date:
    if return_month>expected_month:
        if expected_year==return_year:
            print((30*(return_month-expected_month)-(return_date-expected_date))*500)
        else:
            if expected_year<=return_year:
               print("fine", 10000)
 

            