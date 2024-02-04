Python tkinter:

import tkinter as tk
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile
import PyPDF2 # to extract text from pdf

root = tk.Tk()   # begining of our interface

root.mainloop() # end command of interface

# all elements we put between this 2 lines  
# root=tk.Tk() and root.mainloop() will apear
# inside our window object 

# to precise the dimention of our window
# object we create a variable called canvas
# then we divide the window to 3 imaginary
# column with Canvas.grid() to place our 
#elements precisely

canvas = tk.Canvas(root, width=600, height=300)

Canvas.grid(columnspan=3)

# now To place an image we create a new
# variable : logo 

logo = Image.open(‘file.png’) 

# then we convert this pillow image to 
# tkinter image by typing this :

logo= ImageTk.PhotoImage(logo)

# then we place the image inside a label 
# widget to apear :

logo_label = tk.Label(image=logo)
logo_label.image=logo
logo_label.grid(column=1, row=0)

# to add instruction text :

instructions = tk.Label(root, text=“Select a PDF file on your computer”, font=“Raleway”)

instructions.grid(columnspan=3 , column=0,row=1)

# to add a browse button that change its caption : 

browse_text = tk.StringVar()

browse_btn = tk.Button(root,textvariable =browse_text, command=lambda:open_file(), font=“Raleway” ,bg=“#20bebe”,fg=“white”, height=2, width=15)

browse_text.set(“Browse”)

browse_btn.grid(column=1,row=2)

# then we add a fuction in the beginning that will
# be lunched when we push the button due to the
# command  =lambda:open_file()
# to open browser and chose a file on pc
# need now to import askopenfile from 
# tkinter.filedialog

def open_file():
    browse_text.set(“loading…”) # change caption 
                                                     # butn to loading
    file=askopenfile(parent=root,mode=‘rb’,title=“choose a file”,filetype=[(“Pdf file”, “*.pdf”)])

if file:                  # if file is selected
     read_pdf=PyPDF2.PdfFileReader(file) 
                             # read file and store it in vars   
                             # read_pdf
     page = read_pdf.getPage(0)
     page_content = page.extractText()

     # now writing the content in a text box :

      text_box = tk.Text(root,height=10 ,width=50, 
      padx=15, pady=15)

      text_box.insert(1.0, page_content)
      text_box.grid(column=1, row=3)

      # at the end reset caption of btn to browse:

       browse_text.set(“Browse”)

