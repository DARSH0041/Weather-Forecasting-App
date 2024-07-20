import requests
from tkinter import *
from tkinter import messagebox
from Search import ServicesPage
#from PIL import ImageTk, Image
def show_page(page):
    app.grid_remove()
    page.grid(row=1, column=0, columnspan=4, sticky="nsew")
    #page.grid(fill="both", expand=True)
def navigate_to(page):
    messagebox.showinfo("Navigation", f"You clicked {page}")
app=Tk()
app.title('Weather Application')
app.config(bg='black')
#___________________________________________________obj_________________________________________________________________
search=ServicesPage(app)
home_frame = Frame(app, bg="white")
#____________________________________________________nav________________________________________________________________
menu_bar =Menu(app)
"""mainmenu_bar=Menu(app)
home_menu=Menu(mainmenu_bar)"""
# Create the "Home" menu
home_menu = Menu(menu_bar, tearoff=0)
home_menu.add_command(label="Home Page", command=lambda: show_page(search))
menu_bar.add_cascade(label="🏠", menu=home_menu)

# Create the "About" menu
#image=PhotoImage(file='Home_icon.png')
about_menu =Menu(menu_bar, tearoff=0)
about_menu.add_command(label="Company", command=lambda: navigate_to("About - Company"))
about_menu.add_command(label="Team", command=lambda: navigate_to("About - Team"))
menu_bar.add_cascade(label="About", menu=about_menu)

# Create the "Contact" menu
contact_menu =Menu(menu_bar, tearoff=0)
contact_menu.add_command(label="Email", command=lambda: navigate_to("Contact - Email"))
contact_menu.add_command(label="Phone", command=lambda: navigate_to("Contact - Phone"))
menu_bar.add_cascade(label="Contact", menu=contact_menu)

# Set the menu bar as the main menu of the root window
app.config(menu=menu_bar)
#________________________________________________________canvas_________________________________________________________
"""home_icon=PhotoImage(file='Home_icon.png')
setting_icon=PhotoImage(file='setting_icon.png')
home_button=Button(text='Home',width=22,relief=FLAT,image=home_icon)
home_button.grid(column=0,row=0)
home_lable=Label(text='Wather Forcasting',width=54,font=("Courier",13))
home_lable.grid(column=1,row=0,columnspan=5)
setting_button=Button(text='setting',width=22,image=setting_icon,relief=FLAT)
setting_button.grid(column=6,row=0)"""

app.mainloop()