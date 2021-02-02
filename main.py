from tkinter import *
from custom_widget import ImgButton


def testText(parent):
    text_widget = Text(parent)
    text_widget.pack(side=LEFT, fill=BOTH)
    for i in range(10):
        text_widget.window_create(INSERT, window=Button(text_widget, text=f"{i:03d}"))
    text_widget.configure(state="disabled")
    # text_widget.configure(state="normal")
    return

######################################################################


def grid_align(parent):
    parent.grid_columnconfigure(0, weight=0)
    parent.grid_columnconfigure(1, weight=3)
    parent.grid_columnconfigure(2, weight=1)
    parent.grid_rowconfigure(0, weight=1)
    parent.grid_rowconfigure(1, weight=2)
    btn_ls = list()
    for i in range(6):
        btn_ls.append(Button(parent, text=f"{i:03d}"))
        btn_ls[-1].grid(column=i % 3, row=i // 3, sticky="nsew")
    return

##########################################################


def test_custom_btn(parent):
    parent.grid_columnconfigure(0, weight=0)
    parent.grid_columnconfigure(1, weight=1)
    parent.grid_columnconfigure(2, weight=1)
    btn = ImgButton(parent, img_normal="ball_normal.png",
                    img_hover="ball_hover.png",
                    img_press="ball_press.png")
    btn.grid(column=0, row=0, sticky="nsew")
    ball = PhotoImage(file="ball_normal.png")
    nor_btn = Button(parent, image=ball, borderwidth=0)
    nor_btn.image = ball
    nor_btn.grid(column=2, row=0, sticky="nsew")
    return

################################################


if __name__ == "__main__":
    root = Tk()
    # testText(root)
    # grid_align(root)
    test_custom_btn(root)
    root.mainloop()
