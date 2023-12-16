def fComission(sales):
  if sales>100000:
    comission=0.1
  else:
    comission=0.05
  earned=comission*sales
  target=sales*0.05
  return earned,target
name=str(input("Enter your name: "))
sales=float(input("Enter sales: "))
earned,target=fComission(sales)
print(f"{name} Your earned comission is: {earned:.2f} and your next years target is: {target:.2f}")