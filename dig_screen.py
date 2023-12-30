import customtkinter
import requests
# import office
from PIL import Image
import registration as reg
import modules.path_to_file as path
from datetime import datetime
import modules.functions as m_func
import subprocess

def start_big_screen()

    '''
        searching time and data
    '''

    # print("main, 17: text_name =", text_name)
    # print("main, 18: text_surname =", text_surname)
    full_time = str(datetime.now())
    # full_time =datetime.utcfromtimestamp(json_list["dt"])
    # print("full_time = ", type(full_time))
    time = full_time.split(".")
    # print("time =", time[0])
    date = time[0].split(" ")[0]  
    # print("date =", date)
    list_date = date.split("-")
    hours = time[0].split(" ")[1]
    # print("hours =", hours)
    # print("main, 26: text_city =", m_func.select(surname = text_surname, name = text_name)[0][1])
    print("surname =", reg.text_surname, "name =", reg.text_name)
    cur_city = m_func.select(surname = reg.text_surname, name = reg.text_name)[0][1]

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

    def count_hours(difference, round = False):
        time1 = hours.split(":")
        h = int(time1[0]) + difference
        # print("TIME IN COUNT HOURS", time1[0])
        if round == True:
            if int(time1[1]) <= 30:
                time1[1] = "00"
            elif int(time1[1]) > 30:
                time1[1] = "00"
                h += 1
        time1 = str(h) + ":" + time1[1]
        return time1

    # print(response.status_code)

    if response.status_code == 200:
        w_data = response.json()
        # print(w_data)
    # else:
        # print("Sorry. I don`t know this city.")

    if response1.status_code == 200:
        w_data1 = response1.json()
        # print(w_data)
    # else:
        # print("Sorry. I don`t know this city. 1")

    if response2.status_code == 200:
        w_data2 = response2.json()
        # print(w_data)
    # else:
    #     print("Sorry. I don`t know this city. 2")

    if response3.status_code == 200:
        w_data3 = response3.json()
        # print(w_data)
    # else:
    #     print("Sorry. I don`t know this city. 3")

    if response4.status_code == 200:
        w_data4 = response4.json()
        # print(w_data)
    # else:
    #     print("Sorry. I don`t know this city. 4")

    if response5.status_code == 200:
        w_data5 = response5.json()
        # print(w_data)
    # else:
    #     print("Sorry. I don`t know this city. 5")

    '''
        creating the app
    '''




    app = customtkinter.CTkToplevel()
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
    menu = canv.create_rectangle((0, 0), (275, 800), fill = "#1f333c")

    button_OK = None

    def hide_search_label(event):
        global button_OK
        search_text.place_forget()
        img_search_label.place_forget()
        button_OK = customtkinter.CTkButton(
            master = app,
            text = "OK",
            bg_color = "#5DA7B1",
            fg_color = "#1f333c",
            command = change_key,
            width = 50,
            height = 50,
            border_color = "white",
            border_width = 2,
            corner_radius = 10
        )
        button_OK.place(x = 1146, y = 31)

    def change_key():
        city = search.get()
        app.destroy()
        subprocess.run(["Python", "main.py"])
        # reg.reg_app.destroy()
        # office.off_app.destroy()
        url = f'https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={apikey}&lang=ua'

    def show_search_label(event):
        search_text.place(x = 970, y = 42)
        img_search_label.place(x = 932, y = 41)

    search = customtkinter.CTkEntry(
        master = app,
        width = 218,
        height = 46,
        corner_radius = 20,
        border_width = 3,
        bg_color = "#5DA7B1",
        fg_color = "#1f333c",
        border_color = "white"
    )   
    search.place(x = 918, y = 31)

    img_search = customtkinter.CTkImage(
        light_image = Image.open(path.path_to_file() + "\\search.png"),
        size = (27, 27) 
    )

    img_search_label = customtkinter.CTkLabel(
        master = app,
        bg_color = "#1f333c",
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
        bg_color = '#1f333c',
        text = "пошук",
        font = font18
    )

    search.bind("<FocusIn>", hide_search_label)
    search.bind("<FocusOut>", show_search_label)

    search_text.place(x = 970, y = 42)

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
            bg_color = "#1f333c",
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
                plus_x = 6
                text = description1
                cur_font = font_time_degrees
            elif count == 3:
                # print("temperature")
                text_color = "#b3d0d6"
                plus_y = 70
                plus_x = 111
                cur_font = font_time_degrees
                text = min_max_temp
            elif count == 4:
                text = f"{temp1}°"
                text_color = "white"
                plus_y = 12
                plus_x = 150
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
    # print("json_list =", json_list)
    json_main = json_list["main"]
    # print("json_main =",json_main)
    json_weather = json_list["weather"][0]
    # print("json_weather =",json_weather)

    json_list1 = w_data1['list'][0]
    # print("json_list1 =", json_list1)
    json_main1 = json_list1["main"]
    # print("json_main1 =",json_main1)
    json_weather1 = json_list1["weather"][0]
    # print("json_weather1 =",json_weather1)

    json_list2 = w_data2['list'][0]
    # print("json_list2 =", json_list2)
    json_main2 = json_list2["main"]
    # print("json_main2 =",json_main2)
    json_weather2 = json_list2["weather"][0]
    # print("json_weather2 =",json_weather2)

    json_list3 = w_data3['list'][0]
    # print("json_list3 =", json_list)
    json_main3 = json_list3["main"]
    # print("json_main3 =",json_main3)
    json_weather3 = json_list3["weather"][0]
    # print("json_weather3 =",json_weather3)

    json_list4 = w_data4['list'][0]
    # print("json_list4 =", json_list4)
    json_main4 = json_list4["main"]
    # print("json_main4 =",json_main4)
    json_weather4 = json_list4["weather"][0]
    # print("json_weather4 =",json_weather4)

    json_list5 = w_data5['list'][0]
    # print("json_list5 =", json_list5)
    json_main5 = json_list5["main"]
    # print("json_main5 =",json_main5)
    json_weather5 = json_list5["weather"][0]
    # print("json_weather5 =",json_weather5)

    '''
        Searching today`s information
    '''

    # round the number of the temperature and change it into Celsium degree
    # get the data we need
    timestamp = json_list["dt"]

    # The time
    timezone = datetime.utcfromtimestamp(json_list["dt"])
    hour = datetime.now().hour
    minute = datetime.now().minute

    # The sunrise

    date_only = datetime.utcfromtimestamp(json_list["dt"]).strftime("%d.%m.%y")

    sunrise_time = datetime.utcfromtimestamp(w_data['city']['sunrise'] + w_data["city"]["timezone"])
    hour_sunrise, minute_sunrise = sunrise_time.hour, sunrise_time.minute
    #
    sunset_time = datetime.utcfromtimestamp(w_data['city']['sunset'] + w_data["city"]["timezone"])
    hour_sunset, minute_sunset = sunset_time.hour, sunset_time.minute


    # The data

    # print information
    # print("timezone =", timezone)
    # print(f"temperature = {temperature}°C")
    # print(f"The date in the {cur_city} = {date_only}")
    # print(f"Sun rises in {cur_city} at {hour_s}:{minute_s} local time")

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
            color = "#1f333c"
        if cur_y == 31:
            temperature = counting_degries(json_main['temp'])
            city = "Поточна позиція"
            time = cur_city
            min_max = f"макс.: {counting_degries(json_main['temp_max'])}°, мін.: {counting_degries(json_main['temp_min'])}°"
            description = json_weather["description"]
        elif cur_y == 164:
            temperature = counting_degries(json_main1['temp'])
            city = "Київ"
            time = str(hour) + ":" + str(minute)
            min_max = f"макс.: {counting_degries(json_main1['temp_max'])}°, мін.: {counting_degries(json_main1['temp_min'])}°"
            description = json_weather1["description"]
        elif cur_y == 297:
            temperature = counting_degries(json_main2['temp'])
            city = "Рим"
            time = count_hours(difference = -1)
            min_max = f"макс.: {counting_degries(json_main2['temp_max'])}°, мін.: {counting_degries(json_main2['temp_min'])}°"
            description = json_weather2["description"]
        elif cur_y == 430:
            temperature = counting_degries(json_main3['temp'])
            city = "Лондон"
            time = count_hours(difference = -2)
            min_max = f"макс.: {counting_degries(json_main3['temp_max'])}°, мін.: {counting_degries(json_main3['temp_min'])}°"
            description = json_weather3["description"]
        elif cur_y == 563:
            temperature = counting_degries(json_main4['temp'])
            city = "Варшава"
            time = count_hours(difference = -1)
            min_max =f"макс.: {counting_degries(json_main4['temp_max'])}°, мін.: {counting_degries(json_main4['temp_min'])}°"
            description = json_weather4["description"]
        elif cur_y == 696:
            temperature = counting_degries(json_main5['temp'])
            city = "Прага"
            time = count_hours(difference = -1)
            min_max = f"макс.: {counting_degries(json_main5['temp_max'])}°, мін.: {counting_degries(json_main5['temp_min'])}°"
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
        text = f"{reg.text_name} {reg.text_surname}",
        text_color = "#1f333c"
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
    text2.place(x = 600, y = 101)

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
    create_label(text1 = f"{counting_degries(json_main['temp'])}°", x1 = 683, y1 = 203, size1 = 80)
    create_label(text1 = json_weather["description"], x1 = 650, y1 = 284, size1 = 30)
    create_label(text1 = f"{counting_degries(json_main['temp_min'])}°", x1 = 670, y1 = 348, size1 = 30)
    create_label(text1 = f"{counting_degries(json_main['temp_max'])}°", x1 = 740, y1 = 348, size1 = 30)

    weekday = timezone.strftime("%a")
    # print("weekday =", weekday)

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
    create_label(text1 = weekday, x1 = 970, y1 = 191, size1 = 18)

    create_label(text1 = date_only, x1 = 936, y1 = 227, size1 = 40)
    create_label(text1 = f"{hour}:{minute}", x1 = 974, y1 = 274, size1 = 30)

    main_frame = customtkinter.CTkFrame(
        master = app,
        width = 818,
        height = 240,
        corner_radius = 20,
        border_width = 5,
        bg_color = "#5DA7B1",
        fg_color = "#5DA7B1",
        border_color = "white"
    )
    main_frame.place(x = 325, y = 430)

    line = customtkinter.CTkFrame(
    master = app,
    width = 817,
    height = 1,
    border_width = 2,
    fg_color = "white",
    bg_color = "white",
    border_color = "#FFFFFF"
    )
    line.place(x = 344, y = 476 + 430)
    create_label(text1 = f"Захід сонця о {hour_sunset}:{minute_sunset}. Очікується {description} приблизно о {m_func.find_hours(cur_hour = hour, cur_day = list_date[-1], cur_month = list_date[1], cur_year = list_date[0], n = 2)[0]}:00", x1 = 346, y1 = 445, size1 = 14)
    create_label(text1 = "Зараз", x1 = 325 + 19, y1 = 430 + 54, size1 = 18)
    create_label(text1 = f"{m_func.find_hours(cur_hour = hour, cur_day = list_date[-1], cur_month = list_date[1], cur_year = list_date[0], n = 3)[0]}:00", x1 = 325 + 116, y1 = 430 + 54, size1 = 18)
    create_label(text1 = f"{m_func.find_hours(cur_hour = hour, cur_day = list_date[-1], cur_month = list_date[1], cur_year = list_date[0], n = 6)[0]}:00", x1 = 325 + 208, y1 = 430 + 54, size1 = 18)
    create_label(text1 = f"{m_func.find_hours(cur_hour = hour, cur_day = list_date[-1], cur_month = list_date[1], cur_year = list_date[0], n = 9)[0]}:00", x1 = 325 + 300, y1 = 430 + 54, size1 = 18)
    create_label(text1 = f"{m_func.find_hours(cur_hour = hour, cur_day = list_date[-1], cur_month = list_date[1], cur_year = list_date[0], n = 12)[0]}:00", x1 = 325 + 392, y1 = 430 + 54, size1 = 18)
    create_label(text1 = f"{m_func.find_hours(cur_hour = hour, cur_day = list_date[-1], cur_month = list_date[1], cur_year = list_date[0], n = 15)[0]}:00", x1 = 325 + 484, y1 = 430 + 54, size1 = 18)
    create_label(text1 = f"{m_func.find_hours(cur_hour = hour, cur_day = list_date[-1], cur_month = list_date[1], cur_year = list_date[0], n = 18)[0]}:00", x1 = 325 + 576, y1 = 430 + 54, size1 = 18)
    create_label(text1 = f"{m_func.find_hours(cur_hour = hour, cur_day = list_date[-1], cur_month = list_date[1], cur_year = list_date[0], n = 21)[0]}:00", x1 = 325 + 668, y1 = 54 + 430, size1 = 18)
    create_label(text1 = f"{m_func.find_hours(cur_hour = hour, cur_day = list_date[-1], cur_month = list_date[1], cur_year = list_date[0], n = 24)[0]}:00", x1 = 325 + 760, y1 = 54 + 430, size1 = 18)

    a_hours = count_hours(difference = 0, round = True)
    a_hour = None
    # print("A_HOURS =", a_hours)
    if a_hours == "23:00":
        a_hour = "00:00"
        # date += 1
    elif a_hours == "24:00" or a_hours == "00:00" or a_hours == "1:00" or a_hours == "0:00":
        a_hour = "00:00"
    elif a_hours == "2:00" or a_hours == "3:00" or a_hours == "4:00":
        a_hour = "03:00"
    elif a_hours == "5:00" or a_hours == "6:00" or a_hours == "7:00":
        a_hour = "06:00"
    elif a_hours == "8:00" or a_hours == "9:00" or a_hours == "10:00":
        a_hour = "09:00"
    elif a_hours == "11:00" or a_hours == "12:00" or a_hours == "13:00":
        a_hour = "12:00"
    elif a_hours == "14:00" or a_hours == "15:00" or a_hours == "16:00":
        a_hour = "15:00"
    elif a_hours == "17:00" or a_hours == "18:00" or a_hours == "19:00":
        a_hour = "18:00"
    elif a_hours == "20:00" or a_hours == "21:00" or a_hours == "22:00":
        a_hour = "21:00"

    # print("a_hour =", a_hour)
    create_label(text1 = f"{counting_degries(json_main['temp'])}°", x1 = 325 + 26, y1 = 430 + 176, size1 = 30)
    create_label(text1 = f"{counting_degries(int(m_func.searching_time_data(list_json = w_data, this_date = date, this_hours = a_hour, n = 3)[1]))}°", x1 = 325 + 120, y1 = 430 + 176, size1 = 30)
    create_label(text1 = f"{counting_degries(int(m_func.searching_time_data(list_json = w_data, this_date = date, this_hours = a_hour, n = 6)[1]))}°", x1 = 325 + 209, y1 = 430 + 176, size1 = 30)
    create_label(text1 = f"{counting_degries(int(m_func.searching_time_data(list_json = w_data, this_date = date, this_hours = a_hour, n = 9)[1]))}°", x1 = 325 + 310, y1 = 430 + 176, size1 = 30)
    create_label(text1 = f"{counting_degries(int(m_func.searching_time_data(list_json = w_data, this_date = date, this_hours = a_hour, n = 12)[1]))}°", x1 = 325 + 498, y1 = 430 + 176, size1 = 30)
    create_label(text1 = f"{counting_degries(int(m_func.searching_time_data(list_json = w_data, this_date = date, this_hours = a_hour, n = 15)[1]))}°", x1 = 325 + 406, y1 = 430 + 176, size1 = 30)
    create_label(text1 = f"{counting_degries(int(m_func.searching_time_data(list_json = w_data, this_date = date, this_hours = a_hour, n = 18)[1]))}°", x1 = 325 + 590, y1 = 430 + 176, size1 = 30)
    create_label(text1 = f"{counting_degries(int(m_func.searching_time_data(list_json = w_data, this_date = date, this_hours = a_hour, n = 21)[1]))}°", x1 = 325 + 682, y1 = 430 + 176, size1 = 30)
    create_label(text1 = f"{counting_degries(int(m_func.searching_time_data(list_json = w_data, this_date = date, this_hours = a_hour, n = 24)[1]))}°", x1 = 325 + 774, y1 = 430 + 176, size1 = 30)

    img1 = m_func.find_images(app1= app, description= description, width= 54, height= 50)
    img2 = m_func.find_images(app1= app, description= m_func.searching_time_data(list_json = w_data, this_date = date, this_hours = a_hour, n = 3)[0], width= 50, height= 50)
    img3 = m_func.find_images(app1= app, description= m_func.searching_time_data(list_json = w_data, this_date = date, this_hours = a_hour, n = 6)[0], width= 50, height= 50)
    img4 = m_func.find_images(app1= app, description= m_func.searching_time_data(list_json = w_data, this_date = date, this_hours = a_hour, n = 9)[0], width= 50, height= 50)
    img5 = m_func.find_images(app1= app, description= m_func.searching_time_data(list_json = w_data, this_date = date, this_hours = a_hour, n = 12)[0], width= 50, height= 50)
    img6 = m_func.find_images(app1= app, description= m_func.searching_time_data(list_json = w_data, this_date = date, this_hours = a_hour, n = 15)[0], width= 50, height= 50)
    img7 = m_func.find_images(app1= app, description= m_func.searching_time_data(list_json = w_data, this_date = date, this_hours = a_hour, n = 18)[0], width= 50, height= 50)
    img8 = m_func.find_images(app1= app, description= m_func.searching_time_data(list_json = w_data, this_date = date, this_hours = a_hour, n = 21)[0], width= 50, height= 50)
    img9 = m_func.find_images(app1= app, description= m_func.searching_time_data(list_json = w_data, this_date = date, this_hours = a_hour, n = 24)[0], width= 50, height= 50)

    img1.place(x = 325 + 19, y = 430 + 104)
    img2.place(x = 325 + 112, y = 430 + 104)
    img3.place(x = 325 + 204, y = 430 + 104)
    img4.place(x = 325 + 296, y = 430 + 104)
    img5.place(x = 325 + 388, y = 430 + 104)
    img6.place(x = 325 + 480, y = 430 + 104)
    img7.place(x = 325 + 572, y = 430 + 104)
    img8.place(x = 325 + 664, y = 430 + 104)
    img9.place(x = 325 + 756, y = 430 + 104)

    m_func.db.close()