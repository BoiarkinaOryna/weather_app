import customtkinter
# import sqlite3
import requests
# import json
import asyncio
from PIL import Image
import office as of
import path_to_file as path

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
app.resizable(height = False, width = False)
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

font_city = customtkinter.CTkFont(
    family = "Roboto Slab",
    size = 16
)
font_time_degrees = customtkinter.CTkFont(
    family = "Roboto Slab",
    size = 12

)

def create_frame(y1, color1, city1, time1, description1, min_max1):
    mini_frame = customtkinter.CTkFrame(
        master = app,
        width = 236,
        height = 101,
        border_width = 2,
        corner_radius = 20,
        bg_color = "#096C82",
        fg_color = color1,
        border_color = "white",
    )
    mini_frame.place(x = 19, y = y1)

    text_color = None
    plus_x = 0
    plus_y = 0
    text = None
    min_max_temp = min_max1
    for count in range(4):
        # print(count)
        if count == 1:
            # print("time")
            text_color = "white"
            plus_y = 33
            plus_x = 14
            text = time1
        elif count == 2:
            # print("description")
            text_color = "#b3d0d6"
            plus_y = 70
            plus_x = 14
            text = description1
        elif count == 3:
            # print("temperature")
            text_color = "#b3d0d6"
            plus_y = 70
            plus_x = 122
            text = min_max_temp
        data = customtkinter.CTkLabel(
            master = app,
            text_color = text_color,
            bg_color = color1,
            text = text,
            font = font_time_degrees,
        )
        print(y1 + plus_y)
        data.place(x = 27 + plus_x, y = y1 + plus_y)

    city = customtkinter.CTkLabel(
        master = app,
        text_color = "white",
        text = city1,
        font = font_city,
        bg_color = color1
    )
    city.place(x = 27, y = y1 + 8)
beg_y = 31
city = None
time = 0
description = "A"
min_max = "0"
for count in range(6):
    cur_y = beg_y + 133 * count
    if count == 0:
        color = "#4599A4"
    else:
        color = "#096C82"
    if cur_y == 31:
        city = "Поточна позиція"
        time = cur_city
        min_max = "1"
        description = "B"
    elif cur_y == 164:
        city = "Київ"
        time = "00"
        min_max = "2"
        description = "C"
    elif cur_y == 297:
        city = "Рим"
        time = "00"
        min_max = "3"
        description = "D"
    elif cur_y == 430:
        city = "Лондон"
        time = "00"
        min_max = "4"
    elif cur_y == 563:
        city = "Варшава"
        time = "00"
        min_max ="5"
        description = "E"
    elif cur_y == 696:
        city = "Прага"
        time = "00"
        min_max = 6
        description = "F"
    create_frame(y1 = cur_y, color1 = color, city1 = city, time1 = time, description1 = description, min_max1 = min_max)

user_img = customtkinter.CTkImage(
    light_image = Image.open(path.path_to_file() + "\\user_img.png"),
    size = (48.48, 50) 
)

font_username = customtkinter.CTkFont(
    family = "Roboto Slab",
    size = 14
)

user_img_label = customtkinter.CTkLabel(
    master= app,
    text = "",
    image = user_img,
    bg_color = "#5DA7B1"
)

user_img_label.place(x = 318, y = 29)

user_label = customtkinter.CTkLabel(
    master= app,
    font = font_username,
    bg_color = "#5DA7B1",
    text = f"{of.user_name._text} {of.user_surname._text}"
)
user_label.place(x = 380, y = 39)
font_c = customtkinter.CTkFont(
    family = "Roboto Slab",
    size = 35
)

text2 = customtkinter.CTkLabel(
    master = app,
    text_color = "white",
    bg_color = "#5DA7B1",
    text = "Поточна позиція",
    font = font_c
)
text2.place(x = 576, y = 101)


# connect.commit()
# connect.close()
app.mainloop()