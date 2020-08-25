import json
import os

for dirName in os.listdir('.'):
    print(dirName)

while True:
    try:
        fileName = input("Enter file name, like 'FileName.json': \t")
        filePointer = open(fileName,encoding='utf-8')
        data = json.load(filePointer)
        filePointer.close()
        break
    except FileNotFoundError:
        print ("File not found, please check and try again")
    except json.decoder.JSONDecodeError:
        print ("How about entering a correct .json file?")

finalDict = {}

for row in data:
    for individualData in row['genres']:
        if individualData['id'] in finalDict:
            continue
        finalDict[individualData['id']] = individualData['name']

print (finalDict)
outputPointer = open('output.json','w')
json.dump(finalDict,outputPointer)
outputPointer.close()
print ("Process Successful\n")
input("Press any key to exit:\t")
