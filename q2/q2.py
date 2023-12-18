instructions,horizontalpos,verticalpos,verticalpos2,aim = [],0,0,0,0
[instructions.append(instruction_line.split()) for instruction_line in open("q2.txt").read().split('\n')]
for instruction in instructions:
    if instruction[0] == "forward":
        horizontalpos += int(instruction[1])
        verticalpos2 += aim*int(instruction[1])
    elif instruction[0] == "down":
        verticalpos += int(instruction[1])
        aim += int(instruction[1])
    else:
        verticalpos -= int(instruction[1])
        aim -= int(instruction[1])
print("Part 1 : ",horizontalpos*verticalpos)
print("Part 2 : ",horizontalpos*verticalpos2)