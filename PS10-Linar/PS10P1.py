def seasonForecast(month):
  if month == "December" or month == "January" or month == "February":
    forecast=0.1
  elif month == "March" or month == "April" or month == "May":
    forecast=0.15
  elif month == "June" or month == "July" or month == "August":
    forecast=0.2
  elif month == "September" or month == "October" or month == "November":
    forecast=0.25
  return forecast

reply=str(input("Start the program? Y/N: "))
while reply == "Y" or reply=="y":
  name=str(input("Enter your name: "))
  month=str(input("Enter the month, with capitalization: "))
  while month!= "January" and month!= "February" and month!= "March" and month!= "April" and month!= "May" and month!= "June" and month!= "July" and month!= "August" and month!= "September" and month!= "October" and month!= "November" and month!= "December":
       print("Try entering the month again")
       month=str(input("Enter the month, with capitalization: "))
  sales=float(input("Enter the sales value: "))
  nextMonthSales=seasonForecast(month)*sales+sales
  print("\nName: ",name, "\nMonth: ",month,"\nNext month's estimated sales: ",nextMonthSales)
  reply=str(input("Do you want to continue? Y/N: "))
