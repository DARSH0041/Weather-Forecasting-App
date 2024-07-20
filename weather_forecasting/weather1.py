import requests
import tkinter as tk
from PIL import ImageTk, Image

def get_weather():
    global result_label,err_label,city_entry
    city_label.destroy()
    get_weather_button.destroy()
    result_label = tk.Label(root, text="", bg='white',justify='center')
   
    err_label = tk.Label(root, text="", bg='white')
    
    city = city_entry.get()
    if not city:
        result_label.config(text="Please enter a city name.")
    
    api_key = '39f674cae465f6dc1b58fc2e48a74914'  # You need to get your API key from a weather API provider
    base_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    
    try:
        response = requests.get(base_url)
        data = response.json()
        
        if data["cod"] == "404":
            result_label.config(text="City not found. Please enter a valid city name.")

        
        weather_info = f"Weather in {city}:\n"
        weather_info += f"Description: {data['weather'][0]['description']}\n"
        weather_info += f"Temperature: {data['main']['temp']}°C\n"
        weather_info += f"Humidity: {data['main']['humidity']}%\n"
        weather_info += f"Wind Speed: {data['wind']['speed']} m/s"
        
        result_label.config(text=weather_info)
        weather_condition = data['weather'][0]['main'].lower()
        weather_bg_images = {'clear': "bg_clear.jpg",'clouds': "bg_cloudy.jpg",'rains': "bg_rainy.jpg",'snow': "bg_snow.jpeg",'haze': "bg_rainy.jpg"}
 
        if weather_condition in weather_bg_images:
            bg_image_path = weather_bg_images[weather_condition]
        else:
        # Default background image if weather condition is not found
            bg_image_path = "bg.jpg"
    
        # Load the selected background image
        bg = ImageTk.PhotoImage(file=bg_image_path)
    
        # Update the background label with the new image
        bg_label.config(image=bg)
        bg_label.image = bg
        w = bg.width()
        h = bg.height()
        root.geometry("%dx%d" % (w,h))
        # Make labels visible
        result_label.pack()
        
    except Exception as e:
        err_label.place(x=0,y=0)
        err_label.config(text=e)

def clear():
    result_label.destroy()
    city_entry.delete(0, 'end')
    err_label.destroy()
    bg = ImageTk.PhotoImage(file="bg.jpg")
    bg_label.config(image=bg)
    bg_label.image = bg
    root.geometry("")
    '''w = bg.width()
    h = bg.height()
    root.geometry("%dx%d" % (w,h))'''
    city_label = tk.Label(root, text="Enter city name:", bg='white', font=('Arial', 12, 'bold'))
    city_label.place(x=0,y=0)
    get_weather_button = tk.Button(root, text="Get Weather", command=get_weather, font=('Arial', 12, 'bold'))
    get_weather_button.place(x=5,y=40)
    
# Create the main application window
root = tk.Tk()
root.title("Weather Forecast")
root.config(bg='yellow')

# Set the background image
bg = ImageTk.PhotoImage(file="bg.jpg")
bg_label = tk.Label(root, image=bg)
bg_label.place(x=0, y=0)

root.geometry("%dx%d" % (200,100)) 

# Create and pack the widgets
city_label = tk.Label(root, text="Enter city name:", bg='white', font=('Arial', 12, 'bold'))
city_label.place(x=10,y=0)

city_entry = tk.Entry(root, width=30,justify="left")
city_entry.place(x=1,y=20)
#button = tk.Button(root, text="Button", )

get_weather_button = tk.Button(root, text="Get Weather", command=get_weather)
get_weather_button.place(x=5,y=42)
clear_weather_button = tk.Button(root, text="X", command=clear)
clear_weather_button.place(x=280,y=20)

# Result labels (initially hidden)
""", font=('Arial', 12, 'bold')font=('Arial', 12, 'bold')"""

# Run the main event loop
root.mainloop()
