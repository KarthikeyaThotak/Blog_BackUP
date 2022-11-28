#Python3.10

# Project: Grouping Same Indices


# Array  of Data
InputList = [[10, 40, 50], [20, 70, 30], [90,30,60]]
OutputList = []
index = 0

for i in range(len(InputList[0])):
    OutputList.append([])
    for j in range(len(InputList)):
        OutputList[index].append(InputList[j][index])
    index = index +1

a, b, c = OutputList[0], OutputList[1], OutputList[2]
print(a,b,c)
