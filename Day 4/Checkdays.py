

def findyear():
    year = int(input("Enter a year"));
    month = int(input("Enter a month number to find how many days:" ))

    days = days_in_month(year,month)
    print(days,"days found in",month,"month")


def days_in_month(year,month):
    month_days=[31,28,31,30,31,30,31,31,30,31,30,31]
    if month > 12 or month<1:
        return "Invalid month"
    if month==2 and is_leap(year):
        return 29
    return month_days[month-1]
def is_leap(year):
    if year % 4 == 0:
        if year % 100 ==0:
            if year % 400 ==0:
                print("leap year")
            else:
                print("Not a leap year")
        else:
            print("leap year ")
    else:
        print("not a leap year")