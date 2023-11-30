response=str(input("Run the program? Y/N  "))
students=0
if(response=="Y" or response=="y"):
  while(response=="Y" or response=="y"):
    name=str(input("Enter name:  "))
    exam1=int(input("Enter first exam: "))
    exam2=int(input("Enter second exam: "))
    students=students+1
    print("Name: ",name,"  Average score: ",(exam1+exam2)/2,"  Number of exam calculations: ",students)
    response=str(input("Do you want to continue? Y/N   "))
else:
  print("Thank you for using this program")




