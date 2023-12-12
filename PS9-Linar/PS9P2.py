def funcHitsAverage(hits,bats):
  FhitsAverage=hits/bats
  return FhitsAverage
players=0
reply=str(input("Do you want to start the program? Y/N: "))
while reply == "Y" or reply == "y":
  name=str(input("Enter player name: "))
  hits=float(input("Enter number of hits: "))
  bats=float(input("Enter number of bats: "))##Float for divison
  hitsAverage=funcHitsAverage(hits,bats)
  players=players+1
  print("Player name: ",name)
  print(f"Batting average: {hitsAverage:.2f}")##2f for 2 decimals 
  print("Number of players entered: ", players)
  reply=str(input("Do you want to continue the program? Y/N: "))

          