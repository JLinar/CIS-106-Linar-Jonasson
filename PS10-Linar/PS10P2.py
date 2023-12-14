def f2RoomCalc(length, width, height):
  footage=2*(length*height+width*height+length*width)
  paintGallon=footage/50 
  return paintGallon
reply=str(input("Start the program? (Y/N) "))
while reply=="Y" or reply=="y":
  length=float(input("Enter the length of the room in feet: "))
  width=float(input("Enter the width of the room in feet: "))
  height=float(input("Enter the height of the room in feet: "))
  gallon=f2RoomCalc(length, width, height)
  print(f"Gallons of paint needed: {gallon:.2f}")
  reply=str(input("Continue the program? (Y/N) "))

