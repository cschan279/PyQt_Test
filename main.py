from tkinter import *
from custom_widget import ImgButton

def testText():
    root = Tk()
    text_widget = Text(root)
    text_widget.pack(side=LEFT, fill=BOTH)
    for i in range(10):
        text_widget.window_create(INSERT, window=Button(text_widget, text=f"{i:03d}"))
    text_widget.configure(state="disabled")
    # text_widget.configure(state="normal")
    root.mainloop()
    return

######################################################################
def grid_align():
    root = Tk()
    root.grid_columnconfigure(0, weight=0)
    root.grid_columnconfigure(1, weight=3)
    root.grid_columnconfigure(2, weight=1)
    root.grid_rowconfigure(0, weight=1)
    root.grid_rowconfigure(1, weight=2)
    btn_ls = list()
    for i in range(6):
        btn_ls.append(Button(root, text=f"{i:03d}"))
        btn_ls[-1].grid(column=i%3, row=i//3, sticky="nsew")
    root.mainloop()
    return

##########################################################


"""def button_change_image(parent):
    global btn, image_normal
    btn = Button(root, image=image_normal, borderwidth=0)
    btn.pack()
    btn.bind("<Enter>", hover_btn)
    btn.bind("<Leave>", leave_btn)
    return


def hover_btn(event):
    print(event)
    btn.configure(image=image_hover)
    btn.image = image_hover
    return


def leave_btn(event):
    print(event)
    btn.configure(image=image_normal)
    btn.image = image_normal
    return"""


################################################


if __name__ == "__main__":
    root = Tk()
    # testText()
    # grid_align()
    """
    image_normal = PhotoImage(file="ball_normal.png")
    image_hover = PhotoImage(file="ball_hover.png")
    image_press = PhotoImage(file="ball_press.png")
    btn = None
    button_change_image(root)
    """
    btn = ImgButton(root, img_normal="ball_normal.png",
                    img_hover="ball_hover.png",
                    img_press="ball_press.png")
    btn.pack()
    root.mainloop()
