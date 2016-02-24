
class Cipher:
    #languageWordsFilePath is a set of all acceptable words in the language
    #keyPath is the path of the file containing the key
    def __init__(self,languageWordsFilePath, keyPath):
        self.dicPath=languageWordsFilePath
        self.keyPath=keyPath
     
    #Given a string and an index, this function will shift each alphabetic character
    #in the string by the mod 26 of the index amount. The returned message will be all in 
    #lower-case form. Shifts are only made on a-z and A-z.
    def StringShifter(self, index, str):
        str=str.lower()
        shiftedStr=""
        for character in str:
            if ord(character)<ord("a") or ord(character)>ord("z"):
                shiftedStr+=character
                continue
            shiftedStr+=chr( (((ord(character)-ord("a"))+index) % 26)+ord("a"))
        return shiftedStr

    #Resets the key path used by this instance
    def setKeyPath(self, keyPath):
        self.keyPath=keyPath
    
    #Reads the message from filePath and decodes it using the keyPath file
    #in the instance and writes the decoded message to the outputPath. The 
    #key should be the same key used for EncodeMessage()
    #Decoding is done by shifting each character to the left by one per the value of the key
    def DecodeMessage(self, filePath,outputPath):
        with open(self.keyPath,"r") as keyFile:
            key=int(keyFile.readline().split()[0])
            with open(filePath,"r") as encodedFile:
                decodedMessage= self.StringShifter(key*(-1),encodedFile.read())
                with open(outputPath,"w") as decodedFile:
                    decodedFile.write(decodedMessage)
    
    #Reads the message from filePath and encodes it using the keyPath file
    #in the instance and writes the encoded message to the outputPath.
    #encoding is done by shifting all charactes a-z A-Z to the right by 
    #one character per value of the key
    def EncodeMessage(self, filePath,outputPath):
        with open(self.keyPath,"r") as keyFile:
            key=int(keyFile.readline().split()[0])
            with open(filePath,"r") as messageFile:
                encodedMessage= self.StringShifter(key,messageFile.read())
                with open(outputPath,"w") as encodedFile:
                    encodedFile.write(encodedMessage)
     
    #This function gets the path of an input file and an output file and 
    #attempts to decode the message in the input file using shift cipher methode
    #and brute force to find the closest match. It uses the dictionary of the 
    #language used in the message to count the number of occurences of the words
    #in the message.
    #
    #encodedFilePath is the path of the file containing the encoded message.
    #BruteForcedOutputPath is the path of the output file. The decoded message
    #will be written to the file.
    #Output file will be written in following form:
    #   <number of valid words in message> :: <decoded message>
    def Decode_BF(self,encodedFilePath,BruteForcedOutputPath):
        with open(self.dicPath,"r") as dicFile:
            wordSet= set(line.strip() for line in dicFile)
        #For each shift the occurence of the valid words are contained in languageOcc[]
        with open(encodedFilePath,"r") as secFile:
            secMessage = secFile.read()
            shiftedString=list(self.StringShifter(i,secMessage) for i in range(0,26))
            languageOcc=[0]*len(shiftedString)
            for i in range(0,len(shiftedString)):
                strWords=shiftedString[i].split()
                for word in strWords:
                    if word in wordSet:
                        languageOcc[i]+=1
        #Writing the most likely answer to the given path
        maxOcc=0
        decodedMessage=""
        for i in range(0,len(languageOcc)):
            if languageOcc[i]>maxOcc:
                maxOcc=languageOcc[i]
                decodedMessage=shiftedString[i]
        with open(BruteForcedOutputPath,"w") as decodedFile:
            decodedFile.write(str(maxOcc)+ ":: "+decodedMessage+"\n")

