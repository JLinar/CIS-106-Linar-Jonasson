#PS4P5
itemCost=float(input("Enter the cost of the item: "))
sellCost=float(input("Enter the selling price of the item: "))
fixedCost=float(input("Enter total fixed cost: "))
breakEven=fixedCost/(sellCost-itemCost)
print(f"Required sale for breaking even is: {breakEven:.2f}")