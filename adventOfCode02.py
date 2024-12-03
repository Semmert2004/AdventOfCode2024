def is_inc_or_dec(input):
    inc = input.copy()
    inc.sort()
    dec = input.copy()
    dec.sort(reverse=True)
    if(inc == input or dec == input):
        return True
    return False

def difference(input):
    i = 0
    while ((i < (len(input)-1))):
        if (abs(input[i]-input[i+1]) < 1 or abs(input[i]-input[i+1]) > 3):
            return False
        else:
            i = i + 1
    return True


def part_1():
    safe = 0
    f = open("day2file.txt", "r")
    for x in f:
        row = x.split(" ")
        for i in range(len(row)):
            row[i] = int(row[i])
        if is_inc_or_dec(row) and difference(row):
            safe = safe + 1
            print (safe)

def part_2():
    safe = 0
    f = open("day2file.txt", "r")
    for x in f:
        row = x.split(" ")
        for i in range(len(row)):
            row[i] = int(row[i])
        if is_inc_or_dec(row) and difference(row):
            safe = safe + 1
        else:
            for i in range(len(row)):
                test = list(row)
                test.pop(i)
                if is_inc_or_dec(test) and difference(test):
                    safe = safe + 1
                    break
    return safe

print(part_2())