# module for selecting a file
from tkinter import *
from tkinter import filedialog
# module for transferring pdf to text
from PyPDF2 import PdfReader
# module for converting text to speech
from gtts import gTTS


def get_file_path():
    global file_path
    file_path = filedialog.askopenfilename(title="Choose PDF file you'd like to convert",
                                           filetypes=(("pdf files", "*.pdf"),
                                                      ("all files", "*.*")))
    window.destroy()


def convert_pdf_to_text():
    global file_path
    # Takes pdf location as an argument and then converts that pdf to text
    reader = PdfReader(file_path)
    pdf_text = ''
    for page in range(len(reader.pages)):
        pdf_text += reader.pages[page].extract_text()
    return pdf_text


def text_to_speech_file():
    global text
    language = 'en'
    converted_file = gTTS(text=text, lang=language, slow=False)
    converted_file.save("Text.mp3")


file_path = ""

window = Tk()
window.title("PDF to Voice Converter")
window.geometry("400x200")
button = Button(text='Choose your pdf file for conversion', command=get_file_path)
button.pack()
window.mainloop()

text = convert_pdf_to_text()
text_to_speech_file()