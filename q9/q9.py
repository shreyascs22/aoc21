heights = open("q9.txt").read().split('\n')
points = []
for i in range(len(heights)):
    for j in range(len(heights[0])):
        if i!=0 and i!=len(heights)-1 and j!=0 and j!=len(heights[0])-1 and heights[i][j] < heights[i+1][j] and heights[i][j] < heights[i-1][j] and heights[i][j] < heights[i][j+1] and heights[i][j] < heights[i][j-1]:
            points.append(int(heights[i][j]))
        elif i==0 and j!=0 and j!=len(heights[0])-1 and heights[i][j] < heights[i+1][j] and heights[i][j] < heights[i][j+1] and heights[i][j] < heights[i][j-1]:
            points.append(int(heights[i][j]))
        elif j==0 and i!=0 and i!=len(heights)-1 and heights[i][j] < heights[i-1][j] and heights[i][j] < heights[i+1][j] and heights[i][j] < heights[i][j+1]:
            points.append(int(heights[i][j]))
        elif i==len(heights)-1 and j!=0 and j!=len(heights[0])-1 and heights[i][j] < heights[i-1][j] and heights[i][j] < heights[i][j+1] and heights[i][j] < heights[i][j-1]:
            points.append(int(heights[i][j]))
        elif j== len(heights[0])-1 and i!=0 and i!=len(heights)-1 and heights[i][j] < heights[i+1][j] and heights[i][j] < heights[i-1][j] and heights[i][j] < heights[i][j-1]:
            points.append(int(heights[i][j]))
        elif i==0 and j==0 and heights[i][j] < heights[i+1][j] and heights[i][j] < heights[i][j+1]:
            points.append(int(heights[i][j]))
        elif i==0 and j==len(heights[0])-1 and heights[i][j] < heights[i+1][j] and heights[i][j] < heights[i][j-1]:
            points.append(int(heights[i][j]))
        elif i==len(heights)-1 and j==0 and heights[i][j] < heights[i][j+1] and heights[i][j] < heights[i-1][j]:
            points.append(int(heights[i][j]))
        elif i==len(heights)-1 and j==len(heights[0])-1 and heights[i][j] < heights[i-1][j] and heights[i][j] < heights[i][j-1]:
            points.append(int(heights[i][j]))
        else:
            continue
print("Part 1 : ",sum(points) + len(points)) 