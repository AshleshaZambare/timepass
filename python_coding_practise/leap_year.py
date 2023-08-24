
year = int(input("enter the year:"))
month = int(input("Enter the month:"))

if year % 100 == 0:
    if year % 400 == 0:
        print("year is leap year")
        if month == 2:
            print("there are 29 days in the month")

elif year % 4 == 0:
    print("given year is leap year")
    if month == 2:
        print("there are 29 days in the month")


else:
    print("year is not a leap year")
    if month == 2:
        print("there are 28 days in the month")

if (month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12):
    print("there are 31 days in month")

elif (month == 4 or month == 6 or month == 9 or month == 11):
    print("there are 30 days in the month")

if month < 1 or month > 12:
    print("invalid month")

