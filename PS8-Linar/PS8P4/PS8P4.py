file=open("fileItems.txt","r")
count=0
totalExtendedP=0
item=str(file.readline().rstrip('\n'))
print("Item \t\t Quantity \t\t Price")
while item !="":
  quantity=float(file.readline())
  price=float(file.readline())
  extendedPrice=quantity*price
  totalExtendedP=totalExtendedP+extendedPrice
  count=count+1
  print(item,"\t\t",f"{quantity:.2f}","\t\t\t",f"{price:.2f}")
  item=str(file.readline().rstrip('\n'))
print(f"Total extended price: {totalExtendedP:.2f}")
##Don't know how to print float variable into a float value with 2 decimals, so I put them inside a text as f"{variable:.2f}" 