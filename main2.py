import slate3k as slate
from tkinter.filedialog import *
import pyttsx3

book = askopenfilename()
with open(book, 'rb') as f:
    doc = slate.PDF(f)
    string_of_text = ''
    for text in doc:
        string_of_text += text
# if "\n\n" in doc[0]:
#     doc[0] = doc[0].replace("\n\n", '. ')


     # s = "\n"
     # if stri==s:
     #    stri = stri.replace()






print(string_of_text)
# print(doc[0])
player = pyttsx3.init()
rate = player.setProperty('rate', 140)
player.say(string_of_text)
player.runAndWait()




