print("Check The given year is leapyear or not!")
year = int(input("Enter a year: "))
if(year%4==0):
  if year%100 == 0:
    if year%400 == 0: 
      print("{} is Leap Year".format(year))
    else: 
      print("{} is not a leap year".format(year))
  else: 
    print("{} is a leap year".format(year))
else: 
   print("{} is not a leap year".format(year))
