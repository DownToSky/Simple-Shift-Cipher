from Simple_Cipher import Cipher

#This is jsut an example:
#Example_Key.txt and LangWords.txt should already exist    
myCipher = Cipher("LangWords.txt","Example_Key.txt")
#Example_Message.txt should already exist   
myCipher.EncodeMessage("Example_Message.txt","Example_EncodedMessage.txt")   
myCipher.DecodeMessage("Example_EncodedMessage.txt","Example_DecodedMessage.txt")     
myCipher.Decode_BF("Example_EncodedMessage.txt","Example_DecodedMessage_BF.txt")