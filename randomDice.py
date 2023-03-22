from tkinter import *
import PIL
from PIL import ImageTk, Image
import random

root = Tk()

root.geometry("600x600")
root.title("Dice Game")
root.configure(background="yellow2")

img = ImageTk.PhotoImage(Image.open("dice14.jpg"))
print(img)

label_player1_title = Label(root, text="Player 1", bg="royal blue", fg="white")
label_player1_title.place(relx=0.2, rely=0.3, anchor=CENTER)

label_player2_title = Label(root, text="Player 2", bg="royal blue", fg="white")
label_player2_title.place(relx=0.8, rely=0.3, anchor=CENTER)

label_player1_score = Label(root, bg="royal blue", fg="white")
label_player1_score.place(relx=0.2, rely=0.4, anchor=CENTER)

label_player2_title = Label(root, bg="royal blue", fg="white")
label_player2_title.place(relx=0.8, rely=0.4, anchor=CENTER)

label_players_time_score = Label(root, bg="chocolate1", fg="white")
label_players_time_score.place(relx=0.5, rely=0.5, anchor=CENTER)

root.mainloop()