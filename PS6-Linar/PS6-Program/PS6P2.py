quantity=int(input("Enter quantity: "))
part=int(input("Enter part number: "))
if(part==11 or part== 55):
  price=1.00
elif(part==80 or part==70):
  price=3.00
elif(part==99):
  price=2.00
else:
  price=5.00
totalCost=quantity*price
print("Part number: ",part,"\nUnit cost: ",price,f"\nTotal cost: {totalCost:.2f}")