import customtkinter
import sqlite3
import requests
import json

city = "Дніпро"
apikey = "6f4d7565a9d7bfbe8be8550a1874dc50"
url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={apikey}'

response = requests.get(url)
if response.status_code == 200:
    w_data = response.json()
    
    temp_min = round(w_data['main']['temp_min'] - 273.15)
    temp_max = round(w_data['main']['temp_max'] - 273.15)
    
    connect = sqlite3.connect("database.db")
    cursor = connect.cursor()
    # cursor.execute("ALTER TABLE Users ADD COLUMS (00:00, 01:00, 02:00, 03:00, 04:00, 05:00, 06:00, 07:00, 08:00, 09:00, 10:00, 11:00, 12:00, 13:00, 14:00, 15:00, 16:00, 17:00, 18:00, 19:00, 20:00, 21:00, 22:00, 23:00)")
    # cursor.execute(
    #     "INSERT INTO Users (00:00, 01:00, 02:00, 03:00, 04:00, 05:00, 06:00, 07:00, 08:00, 09:00, 10:00, 11:00, 12:00, 13:00, 14:00, 15:00, 16:00, 17:00, 18:00, 19:00, 20:00, 21:00, 22:00, 23:00) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
    #     (temp_min, temp_min, temp_min, temp_min, temp_min, temp_min, temp_max, temp_max, temp_max, temp_max, temp_max, temp_max, temp_max, temp_max, temp_max, temp_max, temp_max, temp_max, temp_min, temp_min, temp_max, temp_min)
    #     )
    cursor.execute("ALTER TABLE IF NOT EXISTS Users ADD COLUMN time")
    cursor.execute("INSERT INTO Users (time) VALUE (?)", (temp_min))

app = customtkinter.CTk()
app.config(bg = "#5DA7B1")

app.geometry(f"120x800x85x484")
app.title("big screen")

cursor.execute(f'SELECT 00:00 FROM Users WHERE surname = Бояркіна')
print(cursor.fetchall())
text1 = cursor.fetchall()

text2 = customtkinter.CTkLabel(
    master = app,
    text_color = "white",
    bg_color = "#5DA7B1",
    text = "Особистий кабінет",
)

connect.commit()
connect.close()
app.mainloop()