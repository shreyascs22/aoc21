initialstates = [int(initialstate) for initialstate in open("q6.txt").read().split(',')]
arr = [initialstates.count(i) for i in range(9)]
for i in range(256):
    num = arr.pop(0)
    arr[6] += num
    arr.append(num)
    if i == 79:
        val = sum(arr)
print("Part 1 : ",val)
print("Part 2 : ",sum(arr))