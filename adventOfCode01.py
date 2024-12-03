listA = []
listB = []

def splitrows(input):
    array = input.split("   ")
    listA.append(int(array[0]))
    listB.append(int(array[1]))
    

f = open("demofile.txt", "r")
for x in f:
  splitrows(x)

similarity = 0
for x in range(1000):
   similarity = similarity + (listB.count(listA[x]) * listA[x])
   print (similarity)
