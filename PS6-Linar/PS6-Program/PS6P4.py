quantity=int(input("Enter number of tickets: "))
if(quantity>=25):
  price=50
elif(quantity>=10 and quantity<=24):
  price=60
elif(quantity>=5 and quantity<=9):
  price=70
else:
  price=75
total=price*quantity
print("Number of tickets: ",quantity,f"\nPrice per ticket: {price:.2f}",f"\nTotal cost: {total:.2f}")




