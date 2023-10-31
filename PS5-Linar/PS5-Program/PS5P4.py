name=str(input("Enter item name: "))
itemCost=float(input("Enter item cost: "))
if itemCost>1000:
  warrantee=0.1
else:
  warrantee=0.05
warranteeCost=warrantee*itemCost
total=itemCost+warranteeCost
print("Item name: ",name,f"\n Item price: {itemCost:.2f}",f"\n Warrantee cost: {warranteeCost:.2f}",f"\n Total: {total:.2f}")