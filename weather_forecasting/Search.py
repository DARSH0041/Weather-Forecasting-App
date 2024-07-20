from tkinter import *

class ServicesPage(Frame):
    def __init__(self, master):
        super().__init__(master)
        canvas = Canvas(width=602, height=408, bg='yellow', highlightthickness=0)
        bg_img = PhotoImage(file="bg2.png")
        canvas.create_image(100, 200, image=bg_img)
        city_name = Entry(width=30, justify="center", font=('Arial', 12, 'bold'))
        canvas.create_window(30, 20, window=city_name)
        enter_button=Button(width=30,height=20,text='Search')
        canvas.create_window(50, 30, window=city_name)
        # canvas.create_window(100, 100, window=city_name, anchor='w')
        # city_text = canvas.create_text(100, 130, text="00:00", fill="white")
        canvas.grid(column=0, row=0, columnspan=8)

