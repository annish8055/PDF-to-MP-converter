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
    for line in mytext:
        line = line.strip()
        output = output+" "+line
    # Language in which you want to convert 
    language = 'en'
    # Passing the text and language to the engine, 
    # here we have marked slow=False. Which tells 
    # the module that the converted audio should 
    # have a high speed 
    myobj = gTTS(text=output, lang=language, slow=False) 
    
    # Saving the converted audio in a mp3 file named 
    # welcome 
    myobj.save("welcome.mp3") 
    
if __name__ == "__main__":
    main()