import requests
import tkinter as tk
from PIL import ImageTk, Image
import json

def get_weather():
    global result_label, result1_label, result2_label, result3_label, result4_label, err_label
    
    city = city_entry.get()
    if not city:
        result_label.config(text="Please enter a city name.")
        result_label.pack(pady=10)
        return
    
    api_key = '39f674cae465f6dc1b58fc2e48a74914'
    base_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    
    try:
        response = requests.get(base_url)
        data = response.json()
        
        if data["cod"] == "404":
            result_label.config(text="City not found. Please enter a valid city name.")
            result_label.pack(pady=10)
            return
        
        report = json.dumps(data, indent=4)
        with open("weather_detail.json", "w") as w:
            w.write(report)
        
        weather_city = f"Weather in {city}:"
        weather_info = f"Description: {data['weather'][0]['description']}"
        weather_temperature = f"Temperature: {data['main']['temp']}°C"
        weather_humidity = f"Humidity: {data['main']['humidity']}%"
        weather_wind_speed = f"Wind Speed: {data['wind']['speed']} m/s"
        
        show_weather_page(weather_city, weather_info, weather_temperature, weather_humidity, weather_wind_speed, data['weather'][0]['main'].lower())
        
    except Exception as e:
        err_label.config(text=str(e))
        err_label.pack(pady=10)

def show_weather_page(weather_city, weather_info, weather_temperature, weather_humidity, weather_wind_speed, weather_condition):
    weather_bg_images = {
        'clear': "New folder/bg_clear.jpg",
        'clouds': "New folder/bg_cloudy.jpg",
        'rain': "New folder/bg_rainy.jpg",
        'snow': "New folder/bg_snow.jpeg",
        'haze': "New folder/bg_rainy.jpg"
    }

    bg_image_path = weather_bg_images.get(weather_condition, "New folder/bg2.jpg")
    
    weather_page = tk.Toplevel(root)
    weather_page.title("Weather Details")
    
    bg = ImageTk.PhotoImage(file=bg_image_path)
    bg_label = tk.Label(weather_page, image=bg)
    bg_label.image = bg  # Keep a reference to avoid garbage collection
    bg_label.place(x=0, y=0)
    
    w = bg.width()
    h = bg.height()
    weather_page.geometry(f"{w}x{h}")
    
    result_label = tk.Label(weather_page, text=weather_city, bg='white', justify='center', font=('Arial', 16, 'bold'))
    result1_label = tk.Label(weather_page, text=weather_info, bg='white', justify='center', font=('Arial', 14))
    result2_label = tk.Label(weather_page, text=weather_temperature, bg='white', justify='center', font=('Arial', 14))
    result3_label = tk.Label(weather_page, text=weather_humidity, bg='white', justify='center', font=('Arial', 14))
    result4_label = tk.Label(weather_page, text=weather_wind_speed, bg='white', justify='center', font=('Arial', 14))
    
    result_label.pack(pady=10)
    result1_label.pack(pady=5)
    result2_label.pack(pady=5)
    result3_label.pack(pady=5)
    result4_label.pack(pady=5)
    
    back_button = tk.Button(weather_page, text="Back", command=weather_page.destroy, font=('Arial', 12, 'bold'))
    back_button.pack(pady=10)

def clear():
    try:
        result_label.destroy()
        err_label.destroy()
    except Exception:
        pass
    
    city_entry.delete(0, tk.END)
    
    bg = ImageTk.PhotoImage(file="New folder/bg2.jpg")
    bg_label.config(image=bg)
    bg_label.image = bg
    w = bg.width()
    h = bg.height()
    root.geometry(f"{w}x{h}")

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
root.geometry(f"{w}x{h}")

# Create and pack the widgets
city_label = tk.Label(root, text="Enter city name:", bg='white', font=('Arial', 12, 'bold'))
city_label.pack(pady=10)

city_entry = tk.Entry(root, width=30, justify="center", font=('Arial', 12, 'bold'))
city_entry.pack(pady=5)

get_weather_button = tk.Button(root, text="Get Weather", command=get_weather, font=('Arial', 12, 'bold'))
get_weather_button.pack(pady=10)

clear_weather_button = tk.Button(root, text="Clear", command=clear, font=('Arial', 12, 'bold'))
clear_weather_button.pack(pady=5)

# Result labels (initially hidden)
result_label = tk.Label(root, text="", bg='white', justify='center', font=('Arial', 16, 'bold'))
err_label = tk.Label(root, text="", bg='white', font=('Arial', 12, 'bold'), fg='red')

# Run the main event loop
root.mainloop()
