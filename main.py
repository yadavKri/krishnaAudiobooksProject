import pyttsx3
import PyPDF2

book = open('fuck.pdf', 'rb')
pdfReader = PyPDF2.PdfReader(book)

# pagesCount = pdfReader.numPages
t = len(pdfReader.pages)
# print(pagesCount)
print(t)

speaker = pyttsx3.init()
# speaker.say('जिंदगी के बहुत सारे फलसफो को अपने में समेटे यह किताब मन की शांति पाने, परिवार में प्यार बढ़ाने और तरक्की करने के तरीके बताती है। ')

""" for set a RATE of reading..."""
rate = speaker.getProperty('rate')   # getting details of current speaking rate
print(rate)                        # printing current voice rate
speaker.setProperty('rate', 140)     # setting up new voice rate

# starting_page = pdfReader.getPage(8)
starting_page = pdfReader.pages[79]
text = starting_page.extract_text()
print(text)
speaker.say(text)
speaker.runAndWait()
