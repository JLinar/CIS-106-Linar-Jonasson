def array(names,exam):
  for index in range(len(names)):
      print(names[index]+': has score '+ str(exam[index]))

names = ["Name1", "Name2", "Nam3", "Name4", "Nam5","Name6","Name7","Name8","Name9","Name10"]
exam=[10,20,30,40,50,60,70,80,90,100]

def main():
  array(names,exam)

main()