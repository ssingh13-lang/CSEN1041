year = int(input("Enter a year: "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("Leap Year")
else:
    print("Not a Leap Year")

# output

Enter a year: 2024
Leap Year

Enter a year: 1900
Not a Leap Year

Enter a year: 2000
Leap Year

Enter a year: 2023
Not a Leap Year
