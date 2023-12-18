import customtkinter
# import sqlite3
import requests
# import json
# import asyncio
import office
from PIL import Image
from registration import text_surname, text_name
import modules.path_to_file as path
from datetime import datetime
import modules.functions as m_func

'''
    searching time and data
'''

print("main, 17: text_name =", text_name)
print("main, 18: text_surname =", text_surname)
full_time = str(datetime.now())
print("full_time = ", type(full_time))
time = full_time.split(".")
print("time =", time[0])
hours = time[0].split(" ")
print("hours =", hours[1])
print("main, 23: text_city =", m_func.select(surname = text_surname, name = text_name)[0][1])
cur_city = m_func.select(surname = text_surname, name = text_name)[0][1]

'''
    api creation
'''

apikey = "6f4d7565a9d7bfbe8be8550a1874dc50"
url = f'https://api.openweathermap.org/data/2.5/forecast?q={cur_city}&appid={apikey}&lang=ua'
url1 = f"https://api.openweathermap.org/data/2.5/forecast?q=kyiv&appid={apikey}&lang=ua"
url2 = f"https://api.openweathermap.org/data/2.5/forecast?q=rome&appid={apikey}&lang=ua"
url3 = f"https://api.openweathermap.org/data/2.5/forecast?q=london&appid={apikey}&lang=ua"
url4 = f"https://api.openweathermap.org/data/2.5/forecast?q=warsaw&appid={apikey}&lang=ua"
url5 = f"https://api.openweathermap.org/data/2.5/forecast?q=prague&appid={apikey}&lang=ua"

response = requests.get(url)
response1 = requests.get(url1)
response2 = requests.get(url2)
response3 = requests.get(url3)
response4 = requests.get(url4)
response5 = requests.get(url5)

def counting_degries(F):
    celsius = round(F - 273.15)
    return celsius 
def count_hours(difference):
    time = hours[1].split(":")
    h = int(time[0]) + difference
    print(time[1])
    time = str(h) + ":" + time[1]
    return time

print(response.status_code)

if response.status_code == 200:
    w_data = response.json()
    # print(w_data)
else:
    print("Sorry. I don`t know this city.")

if response1.status_code == 200:
    w_data1 = response1.json()
    # print(w_data)
else:
    print("Sorry. I don`t know this city. 1")

if response2.status_code == 200:
    w_data2 = response2.json()
    # print(w_data)
else:
    print("Sorry. I don`t know this city. 2")

if response3.status_code == 200:
    w_data3 = response3.json()
    # print(w_data)
else:
    print("Sorry. I don`t know this city. 3")

if response4.status_code == 200:
    w_data4 = response4.json()
    # print(w_data)
else:
    print("Sorry. I don`t know this city. 4")

if response5.status_code == 200:
    w_data5 = response5.json()
    # print(w_data)
else:
    print("Sorry. I don`t know this city. 5")

'''
    creating the app
'''

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
    border_color = "white"
)   
search.place(x = 918, y = 31)

img_search = customtkinter.CTkImage(
    light_image = Image.open(path.path_to_file() + "\\search.png"),
    size = (27, 27) 
)

img_search_label = customtkinter.CTkLabel(
    master = app,
    bg_color = "#096C82",
    text = "",
    image = img_search
)
img_search_label.place(x = 932, y = 41)

font18 = customtkinter.CTkFont(
    family = "Roboto Slab",
    size = 18
)
search_text = customtkinter.CTkLabel(
    master = app,
    width = 66,
    height = 10,
    bg_color = '#096C82',
    text = "пошук",
    font = font18
)
search_text.place(x = 970, y = 47)

font_city = customtkinter.CTkFont(
    family = "Roboto Slab",
    size = 16
)
font_time_degrees = customtkinter.CTkFont(
    family = "Roboto Slab",
    size = 12
)
font50 = customtkinter.CTkFont(
    family = "Roboto Slab",
    size = 50,
)

'''
    Creating frames with information about another cities
'''

def create_frame(y1, color1, city1, time1, description1, min_max1, temp1):
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
    mini_frame.place(x = 16, y = y1)

    text_color = None
    plus_x = 0
    plus_y = 0
    text = None
    min_max_temp = min_max1
    cur_font = font_time_degrees
    for count in range(5):
        # print(count)
        if count == 1:
            # print("time")
            text_color = "white"
            plus_y = 33
            plus_x = 0
            text = time1
            cur_font = font_time_degrees
        elif count == 2:
            # print("description")
            text_color = "#b3d0d6"
            plus_y = 70
            plus_x = 0
            text = description1
            cur_font = font_time_degrees
        elif count == 3:
            # print("temperature")
            text_color = "#b3d0d6"
            plus_y = 70
            plus_x = 122
            cur_font = font_time_degrees
            text = min_max_temp
        elif count == 4:
            text = temp1
            text_color = "white"
            plus_y = 12
            plus_x = 165
            cur_font = font50
        data = customtkinter.CTkLabel(
            master = app,
            text_color = text_color,
            bg_color = color1,
            text = text,
            font = cur_font,
        )
        # print(y1 + plus_y)
        data.place(x = 23 + plus_x, y = y1 + plus_y)


    city = customtkinter.CTkLabel(
        master = app,
        text_color = "white",
        text = city1,
        font = font_city,
        bg_color = color1
    )
    city.place(x = 23, y = y1 + 8)

'''
    Searching information from another cities
'''

json_list = w_data['list'][0]
print("json_list =", json_list)
json_main = json_list["main"]
print("json_main =",json_main)
json_weather = json_list["weather"][0]
print("json_weather =",json_weather)

json_list1 = w_data1['list'][0]
print("json_list1 =", json_list1)
json_main1 = json_list1["main"]
print("json_main1 =",json_main1)
json_weather1 = json_list1["weather"][0]
print("json_weather1 =",json_weather1)

json_list2 = w_data2['list'][0]
print("json_list2 =", json_list2)
json_main2 = json_list2["main"]
print("json_main2 =",json_main2)
json_weather2 = json_list2["weather"][0]
print("json_weather2 =",json_weather2)

json_list3 = w_data3['list'][0]
print("json_list3 =", json_list)
json_main3 = json_list3["main"]
print("json_main3 =",json_main3)
json_weather3 = json_list3["weather"][0]
print("json_weather3 =",json_weather3)

json_list4 = w_data4['list'][0]
print("json_list4 =", json_list4)
json_main4 = json_list4["main"]
print("json_main4 =",json_main4)
json_weather4 = json_list4["weather"][0]
print("json_weather4 =",json_weather4)

json_list5 = w_data5['list'][0]
print("json_list5 =", json_list5)
json_main5 = json_list5["main"]
print("json_main5 =",json_main5)
json_weather5 = json_list5["weather"][0]
print("json_weather5 =",json_weather5)

'''
    Searching today`s information
'''

main_data = json_list["main"]
# round the number of the temperature and change it into Celsium degree
temperature = round(main_data["temp"])
# get the data we need
timestamp = json_list["dt"]

# The time
timezone = datetime.utcfromtimestamp(json_list["dt"])
hour = datetime.now().hour
minute = datetime.now().minute

# The sunrise

date_only = datetime.utcfromtimestamp(json_list["dt"]).strftime("%d.%m.%y")

sunrise_time = datetime.utcfromtimestamp(w_data['city']['sunrise'] + w_data["city"]["timezone"])
hour_s, minute_s = sunrise_time.hour, sunrise_time.minute

# The data

# print information
print("timezone =", timezone)
print(f"temperature = {temperature}°C")
print(f"The date in the {cur_city} = {date_only}")
print(f"Sun rises in {cur_city} at {hour_s}:{minute_s} local time")

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
        temperature = counting_degries(json_main['temp'])
        city = "Поточна позиція"
        time = cur_city
        min_max = f"макс.: {counting_degries(json_main['temp_max'])}, мін.: {counting_degries(json_main['temp_min'])}"
        description = json_weather["description"]
    elif cur_y == 164:
        temperature = counting_degries(json_main1['temp'])
        city = "Київ"
        time = str(hour) + ":" + str(minute)
        min_max = f"макс.: {counting_degries(json_main1['temp_max'])}, мін.: {counting_degries(json_main1['temp_min'])}"
        description = json_weather1["description"]
    elif cur_y == 297:
        temperature = counting_degries(json_main2['temp'])
        city = "Рим"
        time = count_hours(difference = -1)
        min_max = f"макс.: {counting_degries(json_main2['temp_max'])}, мін.: {counting_degries(json_main2['temp_min'])}"
        description = json_weather2["description"]
    elif cur_y == 430:
        temperature = counting_degries(json_main3['temp'])
        city = "Лондон"
        time = count_hours(difference = -2)
        min_max = f"макс.: {counting_degries(json_main3['temp_max'])}, мін.: {counting_degries(json_main3['temp_min'])}"
        description = json_weather3["description"]
    elif cur_y == 563:
        temperature = counting_degries(json_main4['temp'])
        city = "Варшава"
        time = count_hours(difference = -1)
        min_max =f"макс.: {counting_degries(json_main4['temp_max'])}, мін.: {counting_degries(json_main4['temp_min'])}"
        description = json_weather4["description"]
    elif cur_y == 696:
        temperature = counting_degries(json_main5['temp'])
        city = "Прага"
        time = count_hours(difference = -1)
        min_max = f"макс.: {counting_degries(json_main5['temp_max'])}, мін.: {counting_degries(json_main5['temp_min'])}"
        description = json_weather5["description"]
    create_frame(y1 = cur_y, color1 = color, city1 = city, time1 = time, description1 = description, min_max1 = min_max, temp1 = temperature)

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
    text = f"{text_name} {text_surname}"
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

weathger_image = m_func.find_images(app1 = app, description = json_list["weather"][0]["description"], width = 171, height = 159)

weathger_image.place(x = 380, y = 171)

def create_label(text1, x1, y1, size1):
    text_label = customtkinter.CTkLabel(
        master = app,
        text_color = "white",
        bg_color = "#5DA7B1",
        text = text1,
        font = ("Roboto Slab", size1)
    )
    text_label.place(x = x1, y = y1)
    
create_label(text1 = cur_city, x1 = 689, y1 = 162, size1 = 22)
create_label(text1 = counting_degries(json_main['temp']), x1 = 683, y1 = 203, size1 = 80)
create_label(text1 = json_weather["description"], x1 = 663, y1 = 284, size1 = 30)
create_label(text1 = counting_degries(json_main['temp_min']), x1 = 689.84, y1 = 348, size1 = 30)
create_label(text1 = counting_degries(json_main['temp_max']), x1 = 754.44, y1 = 348, size1 = 30)

weekday = timezone.strftime("%a")
print("weekday =", weekday)

if weekday == "Mon":
    weekday = "Понеділок"
elif weekday == "Tue":
    weekday = "Вівторок"
elif weekday == "Wed":
    weekday = "Середа"
elif weekday == "Thu":
    weekday = "Четвер"
elif weekday == "Fri":
    weekday = "П'ятниця"
elif weekday == "Sat":
    weekday = "Субота"
elif weekday == "Sun":
    weekday = "Неділя"
create_label(text1 = weekday, x1 = 956, y1 = 191, size1 = 18)

create_label(text1 = date_only, x1 = 936, y1 = 227, size1 = 40)
create_label(text1 = f"{hour}:{minute}", x1 = 974, y1 = 274, size1 = 30)

print("func db closed")
m_func.db.close()
app.mainloop()