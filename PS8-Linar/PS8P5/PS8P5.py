file=open("fileCredits.txt","r")
students=0
totalTuition=0
name=str(file.readline().rstrip('\n'))
print("Name \t\t Credits \t\t Tuition")
while name !="":
  code=str(file.readline().rstrip('\n'))
  credits=int(file.readline())
  if code=="I":
    tuitionCredit=250.00
  else:
    tuitionCredit=500.00
  tuition=credits*tuitionCredit
  totalTuition=totalTuition+tuition
  students=students+1
  print(name,"\t\t",credits,"\t\t\t\t",tuition)
  name=str(file.readline().rstrip('\n'))
print(f"Total tuition: {totalTuition:.2f}")
print("Number of students: ",students)