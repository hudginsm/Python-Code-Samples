'''
Reading and Writing
author: Marcus Hudgins
version: Python 3
'''
import random as rng
#writes random numbers to file
def writeFile(x,y):
    outFile = open(x,'w')
    for i in range(y):
        randNum = str(rng.randint(1,500))
        outFile.write(randNum)
        outFile.write("\n")
    outFile.close()
#reads random numbers from file
def readFile(x,y):
    inFile = open(x,'r')
    numList = []
    total = 0
    for i in range(y):
        lineNum = int(inFile.readline())
        print(lineNum)
        numList.append(lineNum)
        total += lineNum
    print('There are {0} random numbers.'.format(len(numList)))
    print('Total of all these numbers: {0}'.format(total))
    print('The largest number is: {0}'.format(max(numList)))
    print('The smallest number is: {0}'.format(min(numList)))
    inFile.close()
#main functon that call the other two function
def main():
    x = input('Input a file name: ')
    y = int(input('How many numbers do you want: '))
    writeFile(x,y)
    readFile(x,y)

if __name__ == '__main__':
    main()
