def FextendedPrice(quantity, price):
  extendedPrice = quantity * price
  if extendedPrice > 10000:
    discount = extendedPrice * 0.1
  else:
    discount = 0
  newExtendedPrice = extendedPrice - discount
  return newExtendedPrice
##Although you used a 'main' function in the word IPO, it doesn't seem to be necessary
## in this case
totalExtPrice=0
reply=str(input("Do you want to start the program? Y/N: "))
while reply == "Y" or reply == "y":
  quantity=float(input("Enter the quantity of the item: "))
  price=float(input("Enter the price of the item: "))
  extendedPrice=FextendedPrice(quantity, price)
  totalExtPrice=totalExtPrice+extendedPrice
  print("Quantity\t\tPrice \t\t Ext Price")
  print(quantity,"\t\t",price,"\t\t",extendedPrice)
  reply=str(input("Do you want to continue the program? Y/N: "))
print("The total extended price is: ", totalExtPrice)
          