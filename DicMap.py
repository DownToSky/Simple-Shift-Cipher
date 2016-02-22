

def StringShifter(index, str):
    str=str.lower()
    shiftedStr=""
    for character in str:
        if ord(character)<ord("a") or ord(character)>ord("z"):
            shiftedStr+=character
            continue
        shiftedStr+=chr( (((ord(character)-ord("a"))+index) % 26)+ord("a"))
    return shiftedStr
    
with open("LangWords.txt","r") as dicFile:
    wordSet= set(line.strip() for line in dicFile)
    
with open("SecretMessage.txt","r") as secFile:
        secMessage = secFile.read()
        shiftedString=list(StringShifter(i,secMessage) for i in range(0,26))
        languageOcc=[0]*len(shiftedString)
        for i in range(0,len(shiftedString)):
            strWords=shiftedString[i].split()
            for word in strWords:
                if word in wordSet:
                    languageOcc[i]+=1


#for i in range(0,26):
#    print(str(languageOcc[i])+ ":: "+shiftedString[i]+"\n")

maxOcc=0
decodedMessage=""
for i in range(0,len(languageOcc)):
    if languageOcc[i]>maxOcc:
        maxOcc=languageOcc[i]
        decodedMessage=shiftedString[i]
        
print(str(maxOcc)+ ":: "+decodedMessage+"\n")

