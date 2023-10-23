
myfile = open("tools/Dictionnary.txt", "r")

myline = myfile.readline()

while myline:
    print(myline)
    cleanedLine = myline.lower().strip()
    if cleanedLine.isalpha() and cleanedLine.find("'") == -1 and cleanedLine.find("-") == -1:
        # print(cleanedLine, len(cleanedLine))
        dictfile = open(str(len(cleanedLine)) + ".txt", "a+")
        dictfile.writelines(cleanedLine + "\r\n")
        dictfile.close()
    else:
        print("error", cleanedLine, cleanedLine.isalpha(),
              cleanedLine.find("'"), cleanedLine.find("-"))
        # pass
    myline = myfile.readline()
myfile.close()
