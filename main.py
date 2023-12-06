#write notes for school while watching videos on one monitor
#by Tyson Shannon
import tkinter as tk

window = tk.Tk()
window.title("Note")
window.geometry("200x30")

frame = tk.Frame(window)
frame.pack()

def submit():
    note = entry.get()
    entry.delete(0, tk.END)
    file = open("notes.txt", "a")
    file.write(note+"\n")
    file.close()

entry = tk.Entry(frame)
button = tk.Button(frame, text="Enter", command=lambda:submit())
entry.grid(column=0, row=0)
button.grid(column=1, row=0)

window.mainloop()