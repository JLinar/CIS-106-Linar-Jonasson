#PS5P1
inputChoice=str(input("Enter your item choice: "))
quantity=int(input("Enter the number of items: "))
if inputChoice== "a":
  price=10.00
else:
  price=20.00
extendedPrice=price*quantity
print("Item: ",inputChoice)
print(f"Price: {price:.2f}")
print(f"Extended price: {extendedPrice:.2f}")
