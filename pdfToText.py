# importing required modules 
import PyPDF2 

def convert():
    # creating a pdf file object 
    pdfFileObj = open('./pdf/Moral Stories.pdf', 'rb') 
    filetext = open("./text/file.txt","w")
    # creating a pdf reader object 
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 
    # printing number of pages in pdf file 
    print(pdfReader.numPages) 
    for i in range(pdfReader.numPages):
        # creating a page object 
        pageObj = pdfReader.getPage(i)
        filetext.write(pageObj.extractText())
        # extracting text from page 
        print(pageObj.extractText()) 
    
    # closing the pdf file object 
    pdfFileObj.close() 
