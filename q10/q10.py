chunks = open("q10.txt").read().split('\n')
points_arr1,incomplete_arr,points_arr2 = [],[],[]
pairs,values = {"]":"[","}":"{",")":"(",">":"<"},{"(":1,"[":2,"{":3,"<":4}
for chunk in chunks:
    flag,stack = 0,[]
    for i in range(len(chunk)):
        if chunk[i] == "[" or chunk[i] == "(" or chunk[i] == "{" or chunk[i] == "<":
            stack.append(chunk[i])
        elif pairs[chunk[i]] == stack[len(stack)-1]:
            stack.pop()
        else:
            flag = 1
            points_arr1.append(chunk[i])
            break
    if not flag:
        if len(stack) != 0:
            incomplete_arr.append(stack)
for i in range(len(incomplete_arr)):
    score = 0
    for j in range(len(incomplete_arr[i])-1,-1,-1):
        score = score*5 + values[incomplete_arr[i][j]]
    points_arr2.append(score)
points_arr2 = sorted(points_arr2)
print("Part 1 :",points_arr1.count(")")*3 + points_arr1.count("]")*57 + points_arr1.count("}")*1197 + points_arr1.count(">")*25137)
print("Part 2 :",points_arr2[len(points_arr2)//2])