def readFromFile():
    file = open('testOne.txt')
    line = file.readline()
    while(line!=""):
        print(line)
        line=file.readline()
    file.close()

def readFromFile2():
    file = open('testOne.txt')
    for singleLine in file.readlines():
        print(singleLine)
    file.close()

# write the reversed list back to the file

def readAndWriteReversedContent():
    with open('testOne.txt','r') as reader:
        content = reader.readlines()
        reversed(content)
    with open('testOne.txt','w') as writer:
        for line in list(reversed(content)):
            writer.write(line if line.endswith('\n') else line+'\n')



#readFromFile()
#readFromFile2()
readAndWriteReversedContent()