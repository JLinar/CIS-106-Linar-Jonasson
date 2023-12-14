def fMilesCalc(miles):
  if miles>=30:
    price=12
  elif miles>=20:
    price=10 
  elif miles>=10:
    price=8
  else:
    price=5
  return price
totalPrice=0
response=str(input("Do you want to check ticket price? (Yes or No): "))
while response=="Yes" or response=="yes" or response=="y" or response=="Y":
  name=str(input("Enter the name: "))
  miles=float(input("Enter distance in miles: "))
  price=fMilesCalc(miles)
  totalPrice=totalPrice+price
  print(f"{name}, your ticket price is: {price:.2f}")
  response=str(input("Do you want to check another ticket? (Yes or No): "))
print(f"The total ticket sum is: {totalPrice:.2f}")