print("Chr\tPos")
count = 0
for ch in range(1,23):
    for pos in range(1001):
        if (pos%5 == 0) or (pos%7 == 0):
            print(ch,pos, sep='\t')
            count += 1
for x in range(51):
    if (x%5 == 0) or (x%7 == 0):
        print("X",x, sep = '\t')
        count += 1

for y in range(21):
    if (y%5 == 0) or (y%7 == 0):
        print("Y", y, sep = '\t')
        count += 1
print("totalLines:\t",count)
