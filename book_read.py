#pythonTextToSpeachXversion3
import pyttsx3

#import pdf reader
import PyPDF2

#cast pyttsx3 into speaker var
speaker = pyttsx3.init()

#speaker.say('Macron made me do it.')

#call book
book = open('LPTHW.pdf', 'rb')

#create var and pass book
pdfReader = PyPDF2.PdfFileReader(book)

#init pages
pages = pdfReader.numPages

#test if pages are 306
#print(pages)
#test passed

#create a loop to start from page 33 > end

for num in range(33, pages):
    
    #start from page 33
    page = pdfReader.getPage(num)

    #extract the information off page 32
    text = page.extractText()

    speaker.say(text)
    #make it talk
    speaker.runAndWait()
