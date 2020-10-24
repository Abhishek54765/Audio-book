import pyttsx3
import PyPDF2
from tkinter.filedialog import *

book = askopenfilename()
reader = PyPDF2.PdfFileReader(book)
no_pages = reader.numPages

for num in range(0, no_pages):
    page = reader.getPage(num)
    text = page.extractText()
    type(text)
    length = len(text)
    for ind in range(length):
        if '  ' in text:
            text = text.join(text[ind+1])
        else:
            pass
    print(text)
    
    #player = pyttsx3.init()
    #player.setProperty('rate', 160)
    #player.say(text)
    #player.runAndWait()


