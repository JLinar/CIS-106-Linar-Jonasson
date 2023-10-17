#PS4P1
originPrice = float(input("Please enter stock purchase price: "))
currentPrice = float(input("Enter current stock price: "))
quantity = int(input("Enter number of shares bought: "))
totalValueChange = currentPrice*quantity-originPrice*quantity
print("Total value change of the stock is: ",totalValueChange)
