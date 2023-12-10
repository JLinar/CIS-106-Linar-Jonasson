file1=open("employee.txt","r")
totalB=0
name=str(file1.readline().rstrip('\n'))
print("Name      Salary      Bonus")
while name!="":
  salary=float(file1.readline())
  if salary>=100000:
    rate=0.2
  elif salary>=50000:
    rate=0.15
  else:
    rate=0.1
  bonus=salary*rate
  totalB=totalB+bonus
  
  print(name,"   ",salary,"   ",bonus)
  name=str(file1.readline().rstrip('\n'))
print(f"Total bonus: {totalB:.2f}")