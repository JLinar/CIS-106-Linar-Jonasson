def fScore(score1,score2,score3):
  average=(score1+score2+score3)/3
  return average
def fScoreHandicap(scoreHand1,scoreHand2,scoreHand3):
  averageHandicap=(scoreHand1+scoreHand2+scoreHand3)/3
  return averageHandicap

##Main function is not needed for this program
reply=int(input("Enter 1 for normal scores, 2 for normal and handicapped scores, 3 for just handicapped scores, or 4 to quit: "))
if reply==1:
  name=str(input("Enter the bowler's name: "))
  score1=int(input("Enter score 1: "))
  score2=int(input("Enter score 2: "))
  score3=int(input("Enter score 3: "))
  average=fScore(score1,score2,score3)
  print("The average for ",name,f" is: {average:.2f}")
elif reply==2:
  name=str(input("Enter the bowler's name: "))
  score1=int(input("Enter score 1 for normal: "))
  score2=int(input("Enter score 2 for normal: "))
  score3=int(input("Enter score 3 for normal: "))
  scoreHand1=int(input("Enter score 1 for handicapped: "))
  scoreHand2=int(input("Enter score 2 for handicapped: "))
  scoreHand3=int(input("Enter score 3 for handicapped: "))
  average=fScore(score1,score2,score3)
  averageHand=fScoreHandicap(scoreHand1,scoreHand2,scoreHand3)
  print(f"The average normal for {name} is: {average:.2f}\nAverage handicapped is: {averageHand:.2f}")
elif reply==3:
  name=str(input("Enter the bowler's name: "))
  scoreHand1=int(input("Enter score 1 for handicapped: "))
  scoreHand2=int(input("Enter score 2 for handicapped: "))
  scoreHand3=int(input("Enter score 3 for handicapped: "))
  averageHand=fScoreHandicap(scoreHand1,scoreHand2,scoreHand3)
  print(f"The average handicapped for {name} is: {averageHand:.2f}")