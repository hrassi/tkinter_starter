import tkinter as tk
from PIL import ImageTk # to print photo

bg_colour = "#3d6466"


def load_frame1():
    frame1.pack_propagate(False)  # to prevent the child label element from modifiying
    #                              the parent frame element

    # frame1 widgets(to print logo using pillow library)
    logo_img = ImageTk.PhotoImage(file="RRecipe_logo.png")
    logo_widget = tk.Label(frame1, image=logo_img, bg=bg_colour)
    logo_widget.image = logo_img
    logo_widget.pack()

    # to print a text in frame1 we use tk.Label
    tk.Label(
        frame1,
        text="ready for you random recipe ?",
        bg=bg_colour,
        fg="white",
        font=("TkMenuFont", 14)  # TkMenuFont with size 14
    ).pack()  # call the pack() function to organise
    #                             # everything nicely inside the frame
    # button widget:
    tk.Button(
        frame1,
        text="SHUFFLE",
        font=("TkHeadingFont", 20),
        bg="#28393a",
        fg="white",
        cursor="hand2",  # change the cursor to hand when we hover over button
        activebackground="#badee2",  # change bkgrnd color when we press
        activeforeground="black",  # change forggrnd color when we press
        command=lambda: load_frame2()  # when we press the button will load frame 2
    ).pack(pady=20)  # pady=20 to give space 20 between widgets
def load_frame2():
    print("Hellow Houssam")


# initiallize app
root = tk.Tk()
root.title("HOUSSAM APP")
#root.eval("tk::PlaceWindow . center") #ths line to center window
# the folowing 3 line is to center the window in the screen
x=root.winfo_screenwidth()//2
y=int(root.winfo_screenheight()*0.1)
root.geometry('500x600+'+str(x)+'+'+str(y))

#to print a frame in the window
frame1=tk.Frame(root,width=500,height=600,bg = bg_colour )
frame2=tk.Frame(root,bg = bg_colour ) #autosize frame cz we didint specify width and heigh
frame1.grid(row=0,column=0)
frame2.grid(row=0,column=0)

load_frame1()


# run app
root.mainloop()
