def funcTuition(credit,code):
  newTuition=250*credit if code=="I" or code=="i" else 500*credit 
  return newTuition

totalTuition=0
response=str(input("Start the program? Y/N: "))
while response=="Y" or response=="y":
  name=str(input("Enter student name: "))
  credit=int(input("Enter number of credits: "))
  code=str(input("Enter district code: "))
  while code!="I" and code!="i" and code!="O" and code!="o":
    print("Invalid code") 
    code=str(input("Enter district code: "))
  tuition=funcTuition(credit,code)
  totalTuition=totalTuition+tuition
  print("\nStudent name: ",name,f"\nThe tuition owed is {tuition:.2f}")
  response=str(input("Do you want to continue? Y/N: "))
print(f"The total tuition is {totalTuition:.2f}")