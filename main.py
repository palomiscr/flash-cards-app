from tkinter import *
import pandas, random

BACKGROUND_COLOR = "#B1DDC6"
timer = None
current_entry = None

# checks which file to read
try:
    data = pandas.read_csv("data/words_to_learn.csv")

except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")

words_dic = data.to_dict(orient="records")


# ------------------------------ FLIP CARDS --------------------------------------------#

def flip_card():
    # shows translation of the current card
    canvas.itemconfig(canvas_img, image=back_img_start)
    canvas.itemconfig(language_text, text="English", fill="white")
    canvas.itemconfig(word_showing, text=current_entry["English"], fill="white")


# ------------------------------ GENERATE WORDS --------------------------------------------#

def next_card():
    global timer  # reset the timer every time the user clicks a new card
    window.after_cancel(timer)

    # shows word that the user wants to learn
    canvas.itemconfig(canvas_img, image=front_img_start)
    canvas.itemconfig(language_text, text="French", fill="black")

    # Picks random dictionary entry
    random_entry = random.choice(words_dic)
    global current_entry
    current_entry = random_entry
    canvas.itemconfig(word_showing, text=random_entry["French"], fill="black")

    timer = window.after(3000, flip_card)


def next_card_update():
    # remove current word and csv update
    words_dic.remove(current_entry)
    words_to_learn = pandas.DataFrame(words_dic)
    words_to_learn.to_csv("data/words_to_learn.csv", index=False)
    next_card()


# ------------------------------ UI SETUP --------------------------------------------#
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_img_start = PhotoImage(file="images/card_front.png")
back_img_start = PhotoImage(file="images/card_back.png")
canvas_img = canvas.create_image(400, 263, image=front_img_start)
canvas.grid(row=0, column=0, columnspan=2)

language_text = canvas.create_text(400, 150, text="title", fill="black", font=("Ariel", 30, "italic"))
word_showing = canvas.create_text(400, 263, text="word", fill="black", font=("Ariel", 50, "bold"))

# Buttons
wrong_png = PhotoImage(file="images/wrong.png")
right_png = PhotoImage(file="images/right.png")

wrong_button = Button(image=wrong_png, highlightthickness=0, bg=BACKGROUND_COLOR, bd=0, command=next_card)
wrong_button.grid(row=1, column=0)
right_button = Button(image=right_png, highlightthickness=0, bg=BACKGROUND_COLOR, bd=0, command=next_card_update)
right_button.grid(row=1, column=1)
# ------------------------------ BUSINESS LOGIC --------------------------------------------#

# shows first card and start timer
timer = window.after(3000, flip_card)
next_card()

window.mainloop()
