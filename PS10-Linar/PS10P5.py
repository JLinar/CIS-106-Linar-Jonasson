def fAssessed(conty,marketValue):
  if county=="Cook" or county=="cook":
    percent=0.90
  elif county=="DuPage" or county=="Dupage" or county=="dupage":
    percent=0.80
  elif county=="McHenry" or county=="Mchenry" or county=="mchenry":
    percent=0.75
  elif county=="Kane" or county=="kane":
    percent=0.60
  else:
    percent=0.70
  NewAssessed=percent*marketValue
  return NewAssessed
totalMarket=0
totalAssessed=0
response=str(input("Do you want to assess your home? (Yes or No): "))
while response=="Yes" or response=="yes" or response=="y" or response=="Y":
  county=str(input("Enter the county: "))
  marketValue=float(input("Enter the market value: "))
  assessed=fAssessed(county,marketValue)
  totalMarket=totalMarket+marketValue
  totalAssessed=totalAssessed+assessed
  print(f"\n  County: {county}\n  Market value: {marketValue:.2f}\n  Assessed value: {assessed:.2f}")
  response=str(input("\nDo you want to assess another property? (Yes or No): "))
print(f"The total market value entered is: {totalMarket:.2f}")
print(f"The total assessed value is: {totalAssessed:.2f}")