quantity=int(input("Enter the number of items: "))
cost=float(input("Enter the cost the books: "))
total=quantity*cost
if total>=50:
  shipping=0.00
else:
  shipping=25.00
print("Quantity: ",quantity)
print(f"Total: {total:.2f}")
print(f"Shipping: {shipping:.2f}")
