# Import the required module for text 
# to speech conversion 
from gtts import gTTS
from pdfToText import convert

# This module is imported so that we can 
# play the converted audio 
import os 

# Main Function
def main():
    # The text that you want to convert to audio 
    convert()
    mytext = open("./text/file.txt","r")
    output=""
    finalTextSet = []
    count = 0
    lineCount = 0
    for line in mytext:
        line = line.strip()
        output = output+" "+line
        lineCount = lineCount+1
        if(lineCount == 1000):
            finalTextSet.append(output)
            output = " "
            lineCount = 1

    finalTextSet.append(output)
    print(len(finalTextSet))
    # Language in which you want to convert 
    language = 'en'
    # Passing the text and language to the engine, 
    # here we have marked slow=False. Which tells 
    # the module that the converted audio should 
    # have a high speed 

    mpFilename = "file"
    for finalText in finalTextSet:
        myobj = gTTS(text=finalText, lang=language, slow=False)
        # Saving the converted audio in a mp3 file named 
        # welcome 
        mpFilename = mpFilename+str(count)
        mpFilename = "%s.mp3" % mpFilename
        count = count+1
        myobj.save(mpFilename) 
        mpFilename = "file"
    
if __name__ == "__main__":
    main()
