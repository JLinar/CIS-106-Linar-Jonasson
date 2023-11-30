

response=str(input("Run the program? Y/N  "))
totalExtended=0
totalSaved=0
while(response=="Y" or response=="y"):
  quantity=int(input("Enter quantity:  "))
  price=float(input("Enter price: "))
  extended=quantity*price
  totalExtended=totalExtended+extended
  if(extended>10000):
    discount=0.25
  else:
    discount=0.1
  saved=extended*discount
  totalSaved=totalSaved+saved
  
  print(f"Extended price: {extended:.2f}",f" \nAmount saved: {saved:.2f}",f" \n Total amount saved:{totalSaved:.2f} ",f" \n Total amount: {totalExtended:.2f}",f"\n  You pay: {totalExtended-totalSaved:.2f}")
  response=str(input("Do you want to continue? Y/N   "))
else:
  print("Thank you for using this program")
