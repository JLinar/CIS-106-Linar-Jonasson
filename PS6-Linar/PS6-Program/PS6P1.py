quantity=int(input("Enter quantity: "))
if(quantity>10000):
  price=10
elif(quantity>=5000 and quantity<=10000):
  price=20
else:
  price=30
tax=price*quantity*0.07
extendedPrice=price*quantity
print(f"Extended price: {extendedPrice:.2f}",f"Tax: {tax:.2f}",f"Total: {extendedPrice+tax:.2f}")