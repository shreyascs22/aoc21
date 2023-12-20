import copy
boards,board,transposed_boards = [],[],[]
# num = [7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1]
num = [38,54,68,93,72,12,33,8,98,88,21,91,53,61,26,36,18,80,73,47,3,5,55,92,67,52,25,40,56,95,9,62,30,31,85,65,14,2,78,75,15,39,87,27,58,42,60,32,41,83,51,77,10,66,70,4,37,6,89,23,16,49,48,63,94,97,86,64,74,82,7,0,11,71,44,43,50,69,45,81,20,28,46,79,90,34,35,96,99,59,1,76,22,24,17,57,13,19,84,29]
file = open("q4.txt")
for line in file:
    line = line.strip()
    if not line:
        if board:
            boards.append(board)
            board = []
    else:
        board.append(list(map(int,line.split())))
if board: 
    boards.append(board)
for board in boards:
    for j in range(5):
        arr = []
        [arr.append(row[j]) for row in board]
        transposed_boards.append(arr)
transposed_boards = [transposed_boards[i:i + 5] for i in range(0, len(transposed_boards), 5)]
bingo = copy.deepcopy(boards)
flag,elefound = 0,False
for n in range(len(num)):
    for board in boards:
        for row in board:
            for ele in range(len(row)):
                if num[n] == row[ele]:
                    row.remove(row[ele])
                    row.insert(ele,-1)
                    elefound = all(element == -1 for element in row)
                    flag = 1
                    break
            if flag:
                flag = 0
                break
        if elefound:
            break
    if elefound:
        break
boardsum = 0
for i in range(5):
    for j in range(5):
        if board[i][j] != -1:
            boardsum += board[i][j]
print(boards.index(board))
print(boardsum*num[n])