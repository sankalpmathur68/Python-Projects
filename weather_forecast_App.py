import tkinter as tk
from PIL import Image, ImageTk
import requests
from io import BytesIO
class WebImage:
     def __init__(self, url):
          u = requests.get(url)
          self.image = ImageTk.PhotoImage(Image.open(BytesIO(u.content)))
          
     def get(self):
          return self.image
class WeatherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Weather Forecast App")
        
        self.api_key = "f403f76188844b52ade133855232008"  # Replace with your WeatherAPI API key
        
        self.location_label = tk.Label(root, text="Enter City:", font=('Helvetica', 14))
        self.location_label.pack(pady=10)
        
        self.location_entry = tk.Entry(root, font=('Helvetica', 12))
        self.location_entry.pack(pady=5)
        
        self.get_weather_button = tk.Button(root, text="Get Weather", command=self.get_weather, font=('Helvetica', 12))
        self.get_weather_button.pack(pady=10)
        
        self.weather_text = tk.Text(root, wrap=tk.WORD, font=('Helvetica', 12))
        self.weather_text.pack(pady=20, padx=10, fill=tk.BOTH, expand=True)
        
    def get_weather(self):
        city = self.location_entry.get()
        if city:
            url = f"https://api.weatherapi.com/v1/current.json?key={self.api_key}&q={city}&aqi=no"
            response = requests.get(url)
            data = response.json()
            
            if "error" not in data:
                self.display_weather_data(data)
            else:
                self.weather_text.delete(1.0, tk.END)
                self.weather_text.insert(tk.END, "Error fetching weather data")
        else:
            self.weather_text.delete(1.0, tk.END)
            self.weather_text.insert(tk.END, "Please enter a city")
    
    def display_weather_data(self, data):
        self.weather_text.delete(1.0, tk.END)
        for key, value in data.items():
            if isinstance(value, dict):
                self.weather_text.insert(tk.END, f"{key}:\n")
                for sub_key, sub_value in value.items():
                    print(type(sub_value)==dict)
                    if(type(sub_value)==dict):
                        for sub_key_2, sub_value_2 in sub_value.items():
                            if(sub_key_2=='icon'):
                                pass
                                # WebImage(sub_value_2)
                            else:
                                self.weather_text.insert(tk.END, f"  {sub_key_2}: {sub_value_2}\n")
                    else:
                        self.weather_text.insert(tk.END, f"  {sub_key}: {sub_value}\n")

                    # if(type(sub_value)==dict):
                    #     for sub_key_2, sub_value_2 in value.items():
                    #         if(sub_key_2!='icon'):
                    #             self.weather_text.insert(tk.END, f"  {sub_key_2}: {sub_value_2}\n")
                    # else:
                        # self.weather_text.insert(tk.END, f"  {sub_key}: {sub_value}\n")

            else:
                self.weather_text.insert(tk.END, f"{key}: {value}\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = WeatherApp(root)
    root.mainloop()
