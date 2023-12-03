import customtkinter
# import sqlite3
import requests
# import json
import asyncio
import office as of

cur_city = of.user_city._text.lower()
print(cur_city)

apikey = "S1a7YDlnJmRJ6m44E2cr6wWVH8NfILK1"
url = f'https://api.tomorrow.io/v4/weather/forecast?location={cur_city}&apikey=S1a7YDlnJmRJ6m44E2cr6wWVH8NfILK1'

response = requests.get(url)

async def counting_degries(F):
    celsius = round(F - 32 / 1.8)
    return celsius 

if response.status_code == 200:
    w_data = response.json()
    print(w_data)

else:
    print("Sorry. I don`t know this city.")

app = customtkinter.CTk()
app.config(bg = "#5DA7B1")

app.geometry(f"1200x800x85x484")
app.title("big screen")

canv = customtkinter.CTkCanvas(
    master = app,
    # height = 1,
    # width = 1,
    bg = "#5DA7B1"
    )
canv.pack(anchor = customtkinter.CENTER, expand = True, fill = "both")
menu = canv.create_rectangle((0, 0), (275, 800), fill = "#096C82")

search = customtkinter.CTkEntry(
    master = app,
    width = 218,
    height = 46,
    corner_radius = 20,
    border_width = 3,
    bg_color = "#5DA7B1",
    fg_color = "#096C82",
    placeholder_text = "пошук",
    text_color = "white",
    border_color = "white"
)   
search.place(x = 918, y = 31)

def create_frame(y1, color1):
    mini_frame = customtkinter.CTkFrame(
        master = app,
        width = 236,
        height = 101,
        border_width = 2,
        corner_radius = 20,
        bg_color = "#096C82",
        fg_color = color1,
        border_color = "white",
        # text = city1,
        # text2 = time1
    )
    mini_frame.place(x = 19, y = y1)

beg_y = 31
city = None
time = 0
for count in range(6):
    cur_y = beg_y + 133 * count
    if count == 0:
        color = "#4599A4"
    else:
        color = "#096C82"
    if cur_y == 31:
        city = "Поточна позиція"
        time = cur_city
    elif cur_y == 164:
        city = "Київ"
        # time =
    elif cur_y == 297:
        city = "Рим"
        # time =
    elif cur_y == 430:
        city = "Лондон"
        # time =
    elif cur_y == 563:
        city = "Варшава"
        # time =
    elif cur_y == 696:
        city = "Прага"
        # time =
    create_frame(y1 = cur_y, color1 = color)

# print(cursor.fetchall())
# text1 = cursor.fetchall()
font_c = customtkinter.CTkFont(
    family = "Roboto Slab",
    size = 35
)
text2 = customtkinter.CTkLabel(
    master = app,
    text_color = "white",
    bg_color = "#5DA7B1",
    text = "Поточна позиція",
    font = font_c,

)
text2.place(x = 576, y = 101)


# connect.commit()
# connect.close()
app.mainloop()