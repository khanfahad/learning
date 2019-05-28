tableData = [['apples', 'oranges', 'cherries', 'banana'],
            ['Alice', 'Bob', 'Carol', 'David'],
            ['dogs', 'cats', 'moose', 'goose']]

def printTable(tableData):
    for word in tableData:
        largestWordLen = len(max(sum(tableData,[]),key=len))
    listLen = len(tableData[0])
    tableLen = len(tableData)
    for i in range(0, listLen):
        for j in range(0, tableLen):
            tempword = tableData[j][i]
            print(tempword.rjust(largestWordLen, " "), end = " ")
        print("\n")
printTable(tableData)
