def funcPayrate(code,hours):
  if code=="L" or code=="l":
    rate=25
  elif code=="A" or code=="a":
    rate=30
  elif code=="J" or code=="j":
    rate=50 
  FPay = (hours - 40) * 1.5 * rate + 40 * rate if hours > 40 else hours * rate
  return FPay

totalPay=0
response=str(input("Start the program? Y/N: "))
while response=="Y" or response=="y":
  name=str(input("Enter employee name: "))
  code=str(input("Enter the employee code: "))
  while code!="L" and code!="l" and code!="A" and code!="a" and code!="J" and code!="j":
    print("Invalid code") ##Adding while loop here just in-
    code=str(input("Enter the employee code: "))##Case the user enters invalid code
  hours=float(input("Enter the number of hours worked: "))
  grossPay=funcPayrate(code,hours)
  print(f"The salary is {grossPay:.2f}")
  totalPay=totalPay+grossPay
  response=str(input("Do you want to continue? Y/N: "))
print(f"The total pay is {totalPay:.2f}")