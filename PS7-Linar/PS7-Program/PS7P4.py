#Just realized that I didn't need to use the 'if statements' in these assignments...


response=str(input("Run the program? Y/N  "))
average=0
total=0
employees=0
while(response=="Y" or response=="y"):
  name=str(input("Enter name:  "))
  hours=int(input("Enter hours worked: "))
  rate=int(input("Enter pay rate "))
  if(hours>40):
    pay=40*rate+(hours-40)*1.5*rate
  else:
    pay=hours*rate
  employees=employees+1
  average=(total+pay)/employees
  total=total+pay
  
  print("Name: ",name,f"  Gross pay: {pay:.2f}","  Number of employees counted: ",employees,f"  Average gross pay: {average:.2f}")
  response=str(input("Do you want to continue? Y/N   "))
else:
  print("Thank you for using this program")
