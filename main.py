import customtkinter
import sqlite3
import requests
import json
import asyncio
import registration as reg

city = "Дніпро"
apikey = "S1a7YDlnJmRJ6m44E2cr6wWVH8NfILK1"
url = f'https://api.tomorrow.io/v4/weather/forecast?location=42.3478,-71.0466&apikey=S1a7YDlnJmRJ6m44E2cr6wWVH8NfILK1'

response = requests.get(url)
print(response)

async def counting_degries(F):
    celsius = round(F - 32 / 1.8)
    return celsius 

if response.status_code == 200:
    w_data = response.json()
    
    connect = sqlite3.connect("database.db")
    cursor = connect.cursor()

    print(reg.text_surname)
    cursor.execute(f'SELECT city FROM Users WHERE surname = {reg.text_surname}')
    if reg.text_city == "Dnipro" or reg.text_city == "Lviv" or reg.text_city == "Kyiv" or reg.text_city == "Zaporizhzhia": 
        cursor.execute("CREATE TABLE IF NOT EXISTS Weather (Dnipro TEXT, Lviv TEXT, Kyiv TEXT, Zaporizhzhia TEXT)")
    else:
        try:
            cursor.execute(f"SELECT {reg.text_city} FROM Weather")
        except:
            cursor.execute(f"ALTER TABLE Weather ADD COLUMN {reg.text_city}")

        cursor.execute("INSERT INTO Weather () VALUES (?)", ())

app = customtkinter.CTk()
app.config(bg = "#5DA7B1")

app.geometry(f"120x800x85x484")
app.title("big screen")

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