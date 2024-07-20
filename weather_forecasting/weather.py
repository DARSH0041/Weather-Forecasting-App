import requests
import tkinter as tk
from PIL import ImageTk, Image
import json
def get_weather():
    global result_label, result1_label, result2_label, result3_label, result4_label, err_label
    try:
        result_label.destroy()
        result1_label.destroy()
        result2_label.destroy()
        result3_label.destroy()
        result4_label.destroy()
    except Exception as e:
        result_label = tk.Label(root, text="", bg='white',justify='center')
        result1_label = tk.Label(root, text="", bg='white',justify='center')
        result2_label = tk.Label(root, text="", bg='white',justify='center')
        result3_label = tk.Label(root, text="", bg='white',justify='center')
        result4_label = tk.Label(root, text="", bg='white',justify='center')
        err_label = tk.Label(root, text="", bg='white')
    finally:
        result_label = tk.Label(root, text="", bg='white', justify='center')
        result1_label = tk.Label(root, text="", bg='white', justify='center')
        result2_label = tk.Label(root, text="", bg='white', justify='center')
        result3_label = tk.Label(root, text="", bg='white', justify='center')
        result4_label = tk.Label(root, text="", bg='white', justify='center')
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
        report=json.dumps(data,indent=4)
        with open ("weather_detail.json","w") as w:
            w.write(report)
        weather_city = f"Weather in {city}:"
        weather_info= f"Description:\n {data['weather'][0]['description']}\n"
        weather_Temperature= f"Temperature:\n {data['main']['temp']}°C\n"
        weather_Humidity = f"Humidity:\n {data['main']['humidity']}%\n"
        weather_WindSpeed= f"Wind Speed:\n {data['wind']['speed']} m/s"
        
        result_label.config(text=weather_city)
        result1_label.config(text=weather_info)
        weather_condition = data['weather'][0]['main'].lower()
        weather_bg_images = {'clear': "New folder/bg_clear.jpg",'clouds': "New folder/bg_cloudy.jpg",'rains': "New folder/bg_rainy.jpg",'snow': "New folder/bg_snow.jpeg",'haze': "New folder/bg_rainy.jpg"}
 
        if weather_condition in weather_bg_images:
            bg_image_path = weather_bg_images[weather_condition]
        else:
        # Default background image if weather condition is not found
            bg_image_path = "New folder/bg2.jpg"
    
        # Load the selected background image
        bg = ImageTk.PhotoImage(file=bg_image_path)
    
        # Update the background label with the new image
        bg_label.config(image=bg)
        bg_label.image = bg
        w = bg.width()
        h = bg.height()
        root.geometry("%dx%d" % (w,h))
        result2_label.config(text=weather_Temperature)
        result3_label.config(text=weather_Humidity)
        result4_label.config(text=weather_WindSpeed)
        # Make labels visible
        result_label.place(x=550,y=120)
        result1_label.place(x=200,y=200)
        result2_label.place(x=400,y=200)
        result3_label.place(x=600,y=200)
        result4_label.place(x=800,y=200)
        
    except Exception as e:
        err_label.place(x=1100,y=0)
        err_label.config(text=e)

def clear():
    result_label.destroy()
    result1_label.destroy()
    result2_label.destroy()
    result3_label.destroy()
    result4_label.destroy()
    city_entry.config(text="")
    err_label.destroy()
    bg = ImageTk.PhotoImage(file="bg.jpg")
    bg_label.config(image=bg)
    bg_label.image = bg
    w = bg.width()
    h = bg.height()
    root.geometry("%dx%d" % (w,h))
# Create the main application window
root = tk.Tk()
root.title("Weather Forecast")
root.config(bg='yellow')

# Set the background image
bg = ImageTk.PhotoImage(file="New folder/bg2.jpg")
bg_label = tk.Label(root, image=bg)
bg_label.place(x=0, y=0)
w = bg.width()
h = bg.height()
root.geometry("%dx%d" % (w,h)) 

# Create and pack the widgets
city_label = tk.Label(root, text="Enter city name:", bg='white', font=('Arial', 12, 'bold'))
city_label.pack()

city_entry = tk.Entry(root, width=30,justify="center", font=('Arial', 12, 'bold'))
city_entry.pack()
#button = tk.Button(root, text="Button", )

get_weather_button = tk.Button(root, text="Get Weather", command=get_weather, font=('Arial', 12, 'bold'))
get_weather_button.pack()
clear_weather_button = tk.Button(root, text="X", command=clear, font=('Arial', 12, 'bold'))
clear_weather_button.pack()

# Result labels (initially hidden)


# Run the main event loop
root.mainloop()
