def fMSRPCalc(make,model,code,price):
  if code=="Y":
    discount=0.3
  elif make=="Honda" and model=="Accord":
    discount=0.1
  elif make=="Toyota" and model=="Rav4":
    discount=0.15
  else:
    discount=0.05
  discountPrice=price*discount
  newPrice=price-discountPrice
  tax=newPrice*0.07
  return discountPrice,newPrice,tax
##Was about to complain about being unable to get the IF STATEMENT priorities correctly without making a mess of a code, apparently I could just put Y,car models, else, to get correct priority:) 
##Program will still give 30% discount for electrical Toyota Rav4 and Honda Accord. That should be correct in this context, I believe.
totalMSRP=0
response=str(input("Do you want to compute the MSRP? (Yes or No): "))
while response=="Yes":
  make=str(input("Enter the make: "))
  model=str(input("Enter the model: "))
  code=str(input("Enter the electric code (Y or N): "))
  price=float(input("Enter the price: "))
  discountPrice,newPrice,tax=fMSRPCalc(make,model,code,price)
  totalMSRP=totalMSRP+newPrice+tax
  print(f"The discount is: {discountPrice:.2f}")
  print(f"The new price after tax is: {newPrice+tax:.2f}")
  response=str(input("Do you want to compute the MSRP? (Yes or No): "))
print(f"The total MSRP is: {totalMSRP:.2f}")