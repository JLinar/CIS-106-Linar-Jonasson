def fExamCalc(exam1,exam2,exam3):
  total=exam1+exam2+exam3
  average=total/3
  return total,average

name=str(input("Enter your name: "))
exam1=int(input("Enter your first exam score: "))
exam2=int(input("Enter your second exam score: "))
exam3=int(input("Enter your third exam score: "))
total,average=fExamCalc(exam1,exam2,exam3)
print(f"{name} Your total score is: {total:.2f} and your average is: {average:.2f}")