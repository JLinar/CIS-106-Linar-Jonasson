def array(names):
  for index in range(len(names)):
      print(names[index])


def arrayReverse(names):
  for index in range(len(names)-1,-1,-1):##start,stop,step for the range. -1,-1,-1 will make it read the index backwards. First -1 makes it begin at the end of the list, second -1 makes it go from index10 all the way down to index 0. The stop index is never reached, hence -1 instead of 0. Third -1 is what kind of step it should take, which is to go from index10 to index 0, one negative step at a time.## (names) remain the same as the memory is not changed.
    ##Took me a while to understand that -1,-1,-1 is not in the subject of arrays, but it is for range.##
    print(names[index])

names = ["Name1", "Name2", "Nam3", "Name4", "Nam5","Name6","Name7","Name8","Name9","Name10"]
def main():
  array(names)
  print("\n Reverse\n")
  arrayReverse(names)
main()