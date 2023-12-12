def funcMpG(miles,gallon):
  MpG=miles/gallon
  return MpG
entries=0
reply=str(input("Do you want to start the program? Y/N: "))
while reply == "Y" or reply == "y":
  city=str(input("Enter player destination name: "))
  miles=float(input("Enter miles traveled: "))
  gallon=float(input("Enter gallons used: "))
  milesPG=funcMpG(miles,gallon)
  entries=entries+1
  print("Destination name: ",city)
  print(f"Miles per gallon: {milesPG:.2f}")
  reply=str(input("Do you want to continue the program? Y/N: "))
print("Number of entries made: ", entries)
          