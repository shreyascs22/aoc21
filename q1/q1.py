measurements = open("q1.txt").read().split('\n')
count,sumcount = 0,0
for i in range(1,len(measurements)):
    if int(measurements[i]) > int(measurements[i-1]):
        count += 1
print("Part 1 : ", count)
for i in range(len(measurements)-3):
    if int(measurements[i]) < int(measurements[i+3]):
        sumcount += 1
print("Part 2 : ",sumcount)