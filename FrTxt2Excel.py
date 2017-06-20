#methods for read txt file and convert to excel
import os

class StatistisReader():
    pass

def ReadResults(fileName):
	fileContent = []
	with open(fileName,'r') as f:
		fileContent = f.readlines()
	return fileContent



def ProcessResults(fileContent):
	handler = TitleHandler
	for line in fileContent:
        handler(line)



#if __name__ == '__main__':
file = "30_V.txt"
content = []
content = ReadResults(file)
print(content)






