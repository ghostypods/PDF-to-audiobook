import pdfplumber
from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
from gtts import gTTS


# ---------- Text to Speech ----------
def convert_tts():
    # open file path of pdf
    file_path = askopenfilename(filetypes=[("PDF files", "*.pdf")])

    if file_path:
        text = ""
        # Open the PDF file
        with pdfplumber.open(file_path) as pdf:
            # Extract text from each page
            for page in pdf.pages:
                text += page.extract_text()

        if text:
            # convert text to speech
            tts = gTTS(text=text, lang="en")
            # save the audio as a mp3 file
            output_file = asksaveasfilename(defaultextension=".mp3", filetypes=[("MP3 files", "*.mp3")])

            if output_file:
                tts.save(output_file)
                status_label.config(text="Speech saved successfully!")

            else:
                status_label.config(text="Couldn't save")
        else:
            status_label.config(text="There is no text to convert to speech")
    else:
        status_label.config(text="File not found")


# ---------- GUI ----------
root = Tk()
root.title("PDF Text-to-Speech")

convert_button = Button(root, text='Select PDF to Convert to Speech', command=convert_tts)
convert_button.place(relx=0.5, rely=0.5, anchor=CENTER)

status_label = Label(root, text="")
status_label.place(relx=0.5, rely=0.7, anchor=CENTER)

root.mainloop()
