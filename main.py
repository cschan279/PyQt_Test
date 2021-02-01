from tkinter import *


if __name__ == "__main__":
    root = Tk()
    text_widget = Text(root)
    text_widget.pack(side=LEFT, fill=BOTH)
    for i in range(10):
        text_widget.window_create(INSERT, window=Button(text_widget, text=f"{i:03d}"))
    text_widget.configure(state="disabled")
    # text_widget.configure(state="normal")
    root.mainloop()
