name=str(input("Enter name: "))
salary=float(input("Enter your salary: "))
level=int(input("Enter your job level: "))
if(level>=10):
  rate=0.25
elif(level>=5 and level<=9):
  rate=0.2
else:
  rate=0.1
bonus=salary*rate
print("Name ",name,f"\nBonus: {bonus:.2f}")
