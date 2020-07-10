import pyttsx3
import PyPDF2


speaker = pyttsx3.init()

speaker.say("Please Enter Your Name")
speaker.runAndWait()
name = input("Enter your Name: ")
speaker.say('Hey {} I am Python in your service What you want me to do.'.format(name))
speaker.runAndWait()

task = input("Please Enter what you want me to do: ") 

speaker.say("Okay I Will Read a book for you")
speaker.runAndWait()


speaker.say("Please enter the pdf of a book which you want me to read")
speaker.runAndWait()

book_name = input('Please enter pdf the book you want to listen: ')
book = open(book_name, 'rb')
pdfReader = PyPDF2.PdfFileReader(book)

pages = pdfReader.numPages
speaker.say("This book has {} number of pages, from which page should i start reading".format(pages))
speaker.runAndWait()


page_no = int(input("Input the page no from which you want to listen the book: "))

speaker.say("sir can i start reading")
speaker.runAndWait()

yes = input("Can i start Reading: ")

if yes == "yes":
    for num in range(page_no, pages):
        PageNo = pdfReader.getPage(page_no)
        text = PageNo.extractText()

        speaker.say(text)

        speaker.runAndWait()

else: exit()