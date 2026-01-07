year = int(input("Enter a year "))
while year >= 0:
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("Leap year")
        break
    else:
        print("Not a leap year")
    
