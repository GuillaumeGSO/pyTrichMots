
myfile = open("Dictionnary.txt", "r")

myline = myfile.readline()

while myline :
    cleanedLine = myfile.readline().lower().replace("\r\n", "")
    if cleanedLine.isalpha() and cleanedLine.find("'") == -1 and cleanedLine.find("-") == -1:
        print(cleanedLine, len(cleanedLine))
        dictfile = open(str(len(cleanedLine)) + ".txt", "a+")
        dictfile.writelines(cleanedLine + "\r\n")
        dictfile.close()
    else:
        pass
        #print("error", myline)
    myline = myfile.readline()
myfile.close()  
