
def hilow(names,exam):
  stop=len(names)
  high=-1.0
  low=999
  highname=None
  lowname=None
  for n in range(0,stop,1):
    if exam[n]>high:
      high=exam[n]
      highname=names[n]
    if exam[n]<low:
      low=exam[n]
      lowname=names[n]
  print("Name: ",highname, " Score: ",high)
  print("Name: ",lowname, " Score: ",low)
  
file=open("text.txt","r")
namesX=file.readline()
names=[]
exam=[]
while namesX!="":
  names.append(str(namesX).rstrip("\n"))
  n=float(file.readline())
  exam.append(n)
  namesX=file.readline()
file.close()
hilow(names,exam)