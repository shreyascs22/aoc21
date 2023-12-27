lines = [line.split('|') for line in open("q8.txt").read().split('\n')]
signals = [line[0].strip().split() for line in lines]
outputs = [line[1].strip().split() for line in lines]
signal_lengths,output_lengths = [],[]
instances,sum = 0,0
for signal in signals:
    arr_signal = []
    for i in range(len(signal)):
        arr_signal.append(len(signal[i]))
    signal_lengths.append(arr_signal)

for output in outputs:
    arr_output = []
    for i in range(len(output)):
        arr_output.append(len(output[i]))
    output_lengths.append(arr_output)

for i in range(len(output_lengths)):
    for j in range(len(output_lengths[i])):
        if signal_lengths[i].count(output_lengths[i][j]) == 1:
            instances += 1
print("Part 1 : ",instances)