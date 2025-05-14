import tkinter as tk
import requests

def get_weather():
    city = city_entry.get()
    api_key = "your_api_key_here"  
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    try:
        response = requests.get(url)
        data = response.json()

        if data["cod"] != "404":
            weather = data['weather'][0]['description'].title()
            temp = data['main']['temp']
            result_label.config(text=f"{city.title()}:\n{weather}\n{temp}°C")
        else:
            result_label.config(text="City not found!")
    except:
        result_label.config(text="Error fetching data.")

root = tk.Tk()
root.title("Weather App")
root.geometry("300x250")

tk.Label(root, text="Enter City:", font="Arial 14").pack(pady=10)
city_entry = tk.Entry(root, font="Arial 14")
city_entry.pack(pady=5)

tk.Button(root, text="Get Weather", command=get_weather, font="Arial 14").pack(pady=10)
result_label = tk.Label(root, font="Arial 14")
result_label.pack()

root.mainloop()
