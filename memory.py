import sys

user_input = []

#Takes the input from command line
#Eg: 128 0 8 16 16
for line in sys.stdin:
    user_input.append(line)
    
#Splits and puts its in a list
user_input = [y for x in user_input for y in x.split(' ')]


memorySizeInBytes = int(user_input[0])
printBeginOffset = int(user_input[1])
bytesPerElement = int(user_input[2])
numElementsToPrint = int(user_input[3])
numElementsPerLine = int(user_input[4])

''''
Sample Input:
memorySizeInBytes = 128
printBeginOffset = 0
bytesPerElement = 8
numElementsToPrint = 16
numElementsPerLine = 16
'''


if bytesPerElement == 1:
    totalMemory = ["00"]*memorySizeInBytes
elif bytesPerElement == 2:
    totalMemory = ["0000"]*(memorySizeInBytes//2)
elif bytesPerElement == 4:
    totalMemory = ["00000000"]*(memorySizeInBytes//4)
elif bytesPerElement == 8:
    totalMemory = ["0000000000000000"]*(memorySizeInBytes//8)


totalMemory  = totalMemory[printBeginOffset:]

counter = 0

for index in range(numElementsToPrint):
    counter += 1
    print(totalMemory[index], end = " ")
    if counter == numElementsPerLine:
        print()
        counter = 0
