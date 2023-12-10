principle=float(input("Enter principle amount: "))
rate=float(input("Enter rate of interest: "))
year=1
while year<6:
  yearInterest=principle*rate
  print("Year","   BBalance","  EBalance")
  print(year,"  ",f"{principle:.2f}",f"{principle+yearInterest:.2f}")
  principle=principle+yearInterest
  year=year+1









