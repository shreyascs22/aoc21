lines = open("q3.txt").read().split('\n')
report = [''.join(row[i] for row in lines) for i in range(len(lines[0]))]
gamma_binary,epsilon_binary = "",""
for i in range(len(report)):
    if report[i].count("1") > report[i].count("0"):
        gamma_binary += "1"
        epsilon_binary += "0"
    else:
        epsilon_binary += "1"
        gamma_binary += "0"
print("Part 1 : ",int(gamma_binary,2)*int(epsilon_binary,2))

transpose_arr,arr,o2 = report,lines,[]
i = 0
while(1):
    if len(o2) == 1:
        break
    if transpose_arr[i].count("1") >= transpose_arr[i].count("0"):
        o2 = [str for str in arr if str[i] == "1"]
    else:
        o2 = [str for str in arr if str[i] == "0"]
    arr = o2
    transpose_arr = [''.join(row) for row in zip(*arr)]
    i += 1
transpose_arr,arr,co2 = report,lines,[]
i = 0
while(1):
    if len(co2) == 1:
        break
    if transpose_arr[i].count("1") >= transpose_arr[i].count("0"):
        co2 = [str for str in arr if str[i] == "0"]
    else:
        co2 = [str for str in arr if str[i] == "1"]
    arr = co2
    transpose_arr = [''.join(row) for row in zip(*arr)]
    i += 1
print("Part 2 : ",int(o2[0],2)*int(co2[0],2))