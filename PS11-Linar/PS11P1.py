def fPriceDiscount(quantity,price,discountRate):
  discountValue=quantity*price*discountRate/100
  newPrice=quantity*price-discountValue
  return newPrice,discountValue
quantity=int(input("Enter quantity: "))
price=float(input("Enter price: "))
discountRate=float(input("Enter discount rate: "))
discountedPrice,discount=fPriceDiscount(quantity,price,discountRate)
print(f"The discounted price is: {discountedPrice:.2f}")
print(f"The discount is: {discount:.2f}")