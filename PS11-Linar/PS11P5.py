def fCalc(quantity,price):
  total=quantity*price
  global taxRate
  taxRate=0.07
  return total
def fMain():
  quantity=int(input("Enter the quantity: "))
  price=float(input("Enter the price: "))
  total=fCalc(quantity,price)
  tax=total*taxRate
  print(f"The total is {total:.2f}")
  print(f"Tax is: {tax:.2f}")
fMain()