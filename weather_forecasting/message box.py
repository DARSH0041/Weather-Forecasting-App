import tkinter as tk
from tkinter import messagebox
from Search import ServicesPage
def navigate_to(page):
    messagebox.showinfo("Navigation", f"You clicked {page}")
def show_page(page):
    page.pack(fill="both", expand=True)
# Create the main window
root = tk.Tk()
root.title("Navigation Bar with Dropdown Example")
root.geometry("400x200")
newpage=ServicesPage(root)
# Create the main menu
menu_bar = tk.Menu(root)

# Create the "Home" menu
home_menu = tk.Menu(menu_bar, tearoff=0)
home_menu.add_command(label="Home Page", command=lambda: show_page(newpage))
menu_bar.add_cascade(label="🏠", menu=home_menu)

# Create the "About" menu
image=tk.PhotoImage(file='Home_icon.png')
about_menu = tk.Menu(menu_bar, tearoff=0)
about_menu.add_command(label="Company", command=lambda: navigate_to("About - Company"))
about_menu.add_command(label="Team", command=lambda: navigate_to("About - Team"))
menu_bar.add_cascade(label="About", menu=about_menu)

# Create the "Services" menu with a nested submenu
services_menu = tk.Menu(menu_bar, tearoff=0)
web_dev_menu = tk.Menu(services_menu, tearoff=0)
web_dev_menu.add_command(label="Frontend", command=lambda: navigate_to("Services - Web Dev - Frontend"))
web_dev_menu.add_command(label="Backend", command=lambda: navigate_to("Services - Web Dev - Backend"))
services_menu.add_cascade(label="Web Development", menu=web_dev_menu)

services_menu.add_command(label="Consulting", command=lambda: navigate_to("Services - Consulting"))
menu_bar.add_cascade(label="Services", menu=services_menu)

# Create the "Contact" menu
contact_menu = tk.Menu(menu_bar, tearoff=0)
contact_menu.add_command(label="Email", command=lambda: navigate_to("Contact - Email"))
contact_menu.add_command(label="Phone", command=lambda: navigate_to("Contact - Phone"))
menu_bar.add_cascade(label="Contact", menu=contact_menu)

# Set the menu bar as the main menu of the root window
root.config(menu=menu_bar)

# Run the main loop
root.mainloop()
