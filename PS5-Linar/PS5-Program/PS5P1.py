#PS5P1
quantity=int(input("Enter the number of items: "))
if quantity >= 1000:
  unitPrice=3
else:
  unitPrice=5
tax=unitPrice*quantity*0.07
totalPrice=unitPrice*1.07*quantity
print(f"Quantity: {quantity:.2f}")
print(f"Unit price: {unitPrice:.2f}")
print(f"Extended price: {quantity*unitPrice:.2f}")
print(f"Tax: {tax:.2f}")
print(f"Total: {totalPrice:.2f}")