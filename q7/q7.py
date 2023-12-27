pos = [int(x) for x in open("q7.txt").read().split(',')]
min_sum = sum(pos)
min_sum2 = sum([ele*(ele+1)//2 for ele in pos])
flag1,flag2 = False,False
print(min_sum2)
for ele in range(max(pos)):
    arr = list(map(lambda x : abs(ele-x),pos))
    arr2 = list(map(lambda x : abs(ele-x)*(abs(ele-x)+1)//2,pos))
    if sum(arr) > min_sum and not flag1:
        print("Part 1 : ",min_sum)
        flag1 = True
        if flag2:
            break
    min_sum = sum(arr)
    if sum(arr2) > min_sum2 and not flag2:
        print("Part 2 : ",min_sum2)
        flag2 = True
        if flag1:
            break
    min_sum2 = sum(arr2)