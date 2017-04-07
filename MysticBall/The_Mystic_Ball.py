from tkinter import *
import tkinter.font as font
from tkinter import ttk
import random

class Mystic_ball(ttk.Frame):

    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)
        self.root = parent
        self.root.resizable(0,0)
        self.root.configure(bg="black")
        self.game()

    def game(self):
        self.root.title("Mystic ball game")

        #an image on the top of the window
        self.img = PhotoImage(file="ballpic.png")
        self.image = PhotoImage.subsample(self.img, x=4, y=4)
        self.picHeader = ttk.Label(image=self.image, background="black")
        self.picHeader.grid(columnspan=1, row=0, sticky="n")

        #a header just below the image
        self.headerText = ttk.Label(text="Ask the great orbuculum about the future", font=('Moon', 14, "bold"), foreground="white", background="black")
        self.headerText.grid(columnspan=1, row=1, sticky="n")

        #the widget where the answer will be displayed
        self.aswDis = ttk.Label(relief="ridge", width=50, foreground="white", background="black", font=("Moon", 11))
        self.aswDis.grid(column=0, row=3, pady=50)

        #the function telling the button to generate an answer from the list
        def scrying():
            answerList = ["That's possible...",
                          "The moon will be red and rivers will be still; it's a clear no.",
                          "The great cosmos is saying yes.",
                          "Certainly!",
                          "Maybe yes, maybe no...",
                          "No."]

            ranScry = random.choice(answerList)
            self.aswDis.configure(text=ranScry)

        # button to generate an answer
        self.genBut = Button(text="Scry", command=lambda: scrying(), width=4, height=1, font=('Moon', 11, ), background="white")
        self.genBut.grid(column=0, row=4)


if __name__ == '__main__':
    root = Tk()
    Mystic_ball(root)
    root.mainloop()
