def part_1(input):
 total = 0
 x = True
 while x == True:
    i = input.find("mul(")
    if i == -1:
       x = False
       break
    input = input[i+4:]
    b = input.find(")")
    if b > 7 or input[0:b].find(",") == -1:
      continue
    nums = input[0:b]
    c = nums.split(",")
    total = total + int(c[0]) * int(c[1]) 
 return total

def part_2(input):
 total = 0
 x = True
 while x == True:
    i = input.find("mul(")
    do = input.find("do()")
    dont = input.find("don't()")
    if dont < i and dont != -1:
      input = input[do+4:]
      continue
    if i == -1:
       x = False
       break
    input = input[i+4:]
    b = input.find(")")
    if b > 7 or input[0:b].find(",") == -1:
      continue
    nums = input[0:b]
    c = nums.split(",")
    total = total + int(c[0]) * int(c[1]) 
 return total

f = open("day3text.txt", "r")
g = open("day3text.txt", "r")

print(part_1(f.read()))
print(part_2(g.read()))