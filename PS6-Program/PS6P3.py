money=float(input("Enter investment amount: "))
year=int(input("Enter number of years: "))
if(money>100000 and year==5):
  rate=0.06
elif(money>=50000 and year==10):
  rate=0.05
elif(money>=50000 and year==5):
  rate=0.04
else:
  rate=0.02
interest=money*rate
print(f"Invested: {money:.2f}","Interest rate: ",rate*100,"%", f"\nInterest for first year: {interest:.2f}")



