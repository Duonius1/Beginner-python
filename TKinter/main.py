import tkinter
from tkinter import Entry

window = tkinter.Tk()
window.title("My First GUI Program ")  # Correct way to set the title
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

# Label
my_label = tkinter.Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.config(text="New Text")
my_label.grid(column=0, row=0)
my_label.config (padx = 50, pady = 50)

# Button

def button_clicked():
    print("I got clicked")
    my_label["text"] = Entry.get(input)

button = tkinter.Button(text="Click Me",  command = button_clicked)
button.grid(column=1, row=1)
new_button = tkinter.Button(text="Fuck you",)
new_button.grid(column=2, row = 0)

# Entry

input = Entry(width = 10)
input.grid(column=3, row=2)

window.mainloop()

