def searchEngine(name,searchName):
  stop=len(name)
  missing=-1
  for i in range(0,stop,1):
    if name[i]==searchName:
      missing=i
  return missing

name=[]
batting=[]
file=open("text.txt","r")
nameX=file.readline()
while nameX !="":
  name.append(str(nameX).rstrip("\n"))
  n=float(file.readline())
  batting.append(n)
  nameX=file.readline()
file.close()

response=input("Do you want to search a player? (Y/N) ")
while response=="Y":
  searchName=input("Enter the name of the player you want to search for: ")
  x=searchEngine(name,searchName)
  if x ==-1:
    print("Player not found")
  else:
    print(name[x],"has a batting average of",batting[x])
  response=input("Do you want to search a player? (Y/N)")
