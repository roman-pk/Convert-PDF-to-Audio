# Convert-PDF-to-Audio
First version of my text to speech project which takes a pdf file, converts it to text and then to speech (mp3 file).

- I am using Tkinter to provide a simple GUI to select a file that a user would like to convert
- PdfReader to convert PDF to a text string 
- Google Text-to-Speech (gTTS) library to convert text to spoken mp3 file. 

## List of potential future improvements: 
- GUI: Button that selects the pdf file does not close the GUI window immidietly
- GUI: A progress bar that shows that the text is extracted from the pdf. It can also show the progress status of the text to speech conversion. 
- GUI: A button that allows user to select destination to save the converted audio file.
- Test more PDF documents and make sure that text extracted is clean and does not cause errors. Set up some exception handling.
- Write a function for the save to destination button. 
- GUI: Give users options to adjust gTTS parameters.
