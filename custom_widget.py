from tkinter import Button, Text, PhotoImage


class ImgButton(Button):
    def __init__(self, *args, **kwargs):
        if 'img_normal' in kwargs:
            self.image_normal = PhotoImage(file=kwargs['img_normal'])
            if 'img_hover' in kwargs:
                self.image_hover = PhotoImage(file=kwargs['img_hover'])
                kwargs.pop('img_hover')
            else:
                self.image_hover = PhotoImage(file=kwargs['img_normal'])
            if 'img_press' in kwargs:
                self.image_press = PhotoImage(file=kwargs['img_press'])
                kwargs.pop('img_press')
            else:
                self.image_press = PhotoImage(file=kwargs['img_normal'])
            kwargs.pop('img_normal')
        else:
            raise Exception("No img_normal")
        super().__init__(image=self.image_normal, borderwidth=0, *args, **kwargs)
        self.image = self.image_normal
        self.bind("<Enter>", self.hover_btn)
        self.bind("<Leave>", self.resume_btn)
        self.bind("<Button>", self.press_btn)
        self.bind("<ButtonRelease>", self.resume_btn)
        return

    def hover_btn(self, event):
        print(event)
        self.configure(image=self.image_hover)
        self.image = self.image_hover
        return

    def resume_btn(self, event):
        print(event)
        self.configure(image=self.image_normal)
        self.image = self.image_normal
        return

    def press_btn(self, event):
        print(event)
        self.configure(image=self.image_press)
        self.image = self.image_press
        return
