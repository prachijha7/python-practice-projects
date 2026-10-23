from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = []
flip_timer = None
# ---------------------------- READ FILE ----------------------------- #
try:
    data = pandas.read_csv("./Flash Card Project/data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("./Flash Card Project/data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")
# ---------------------------- REMOVE CARD ----------------------------- #
def is_known():
    to_learn.remove(current_card)
    data  = pandas.DataFrame(to_learn)
    data.to_csv("./Flash Card Project/data/words_to_learn.csv", index=False)
    if to_learn:
        next_card()
    else:
        canvas.itemconfig(canvas_image, image=card_front_img)
        canvas.itemconfig(card_title, text="Congratulations!", fill="black")
        canvas.itemconfig(card_word, text="You learned all the words!", fill="black")
# ---------------------------- CHOOSE CARD ----------------------------- #
def next_card():
    global current_card, flip_timer
    if flip_timer:
        window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(canvas_image, image=card_front_img)
    canvas.itemconfig(card_word, fill="black", text=current_card["French"])
    canvas.itemconfig(card_title, fill="black", text="French")
    flip_timer = window.after(3000,func=flip_card)
# ---------------------------- FLIP CARD ----------------------------- #
def flip_card():
    canvas.itemconfig(canvas_image, image=card_back_img)
    canvas.itemconfig(card_title, fill="white", text="English")
    canvas.itemconfig(card_word, fill="white", text=current_card["English"])
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_front_img = PhotoImage(file="./Flash Card Project/images/card_front.png")
card_back_img = PhotoImage(file="./Flash Card Project/images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"), fill="black")
card_word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"), fill="black")
canvas.grid(row=0, column=0, columnspan=2)

right_img = PhotoImage(file="./Flash Card Project/images/right.png")
known_button = Button( image=right_img, highlightthickness=0, borderwidth=0, relief="flat", command=is_known)
known_button.grid(row=1, column=1)

wrong_image = PhotoImage(file="./Flash Card Project/images/wrong.png")
unknown_button = Button(image=wrong_image, highlightthickness=0, borderwidth=0, relief="flat", command=next_card )
unknown_button.grid(row=1, column=0)

next_card()

window.mainloop()