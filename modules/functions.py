from PIL import Image
import modules.path_to_file as m_path
import customtkinter 
import sqlite3 
# def set_day_night(list_json, data_time):
#     list_json
#     timestamp = (date_time -"0001-01-01T00:00:00Z) * 86400
db = sqlite3.connect("database.db")
cursor = db.cursor()

def find_images(app1, description, width, height, time = "day"):
    print("DESCRIPTION =", description)
    if time == "day":
    
        if description == "легкий дощ" or description == "помірний дощ":
            image = "drizzle_2412695.png"
        elif description == "сніг" or description == "легкий сніг":
            image = "snowy_2412768.png"
        elif description == "дощ":
            image = "rainy_2412747.png"
        elif description == "хмарно" or description == "рвані хмари" or description == "уривчасті хмари" or description == "кілька хмар":
            image = "day_clouds.png"
        elif description == "ясно" or description == "чисте небо":
            image = "clear_sky.png"
        elif description == "гроза" or description == "шторм":
            image = "storm_2412772.png"
        else:
            image = None
    if time == "night":
        if description == "легкий дощ":
            image = "rain_2412733.png"
        elif description == "сніг" or description == "легкий сніг":
            image = "snowy_2412767.png"
        elif description == "дощ":
            image = "night_shower.png"
        elif description == "хмарно" or description == "рвані хмари":
            image = "night_few_clouds.png"
        elif description == "ясно":
            image = "clear_sky.png"
        elif description == "гроза" or description == "шторм":
            image = "snowy_2412767.png"
        else:
            image = "captcha_6741193.png"
    
    image_weather = customtkinter.CTkImage(
        light_image = Image.open(m_path.path_to_file() + f"\\{image}"),
        size = (width, height)
    )
    image_weather_label = customtkinter.CTkLabel(
        master = app1,
        bg_color = "#5DA7B1",
        text = "",
        image = image_weather
    )
    return image_weather_label


def select(surname: str, name: str):
    # print("func: select, SURNAME =", surname)
    # print("func: select, NAME =", name)
    cursor.execute('SELECT * FROM Users WHERE surname = ?', [surname])
    cursor.execute('SELECT * FROM Users WHERE name = ?', [name])
    db.commit()
    return cursor.fetchall()

def find_hours(cur_hour, cur_day, cur_month, cur_year, n):
    cur_day = int(cur_day)
    cur_month = int(cur_month)
    cur_year = int(cur_year)
    print("cur_hour in func =", cur_hour)
    if cur_hour + n <= 23:
        time = cur_hour + n 
    else:
        time = cur_hour
        print("n in find_hours 1 =", n)
        # if n == 2:
        #     n = 3
        # elif n % 3 == 1:
        #     n -= 1
        # elif n % 3 == 2:
        #     n = n - 2
        print("n in find_hours 2 =", n - 1)
        for count in range(n):
            print("count in find_hours =", count)
            time = time + 1
            print("plus 1 hour", time)
            if time >= 23:
                time = 0
                cur_day += 1
                print("plus 1 day", time, cur_day)
                if cur_day > 31:
                    cur_day = 1
                    cur_month += 1
                    print("plus 1 month", time, cur_day, cur_month)
                    if cur_month > 12:
                        cur_month = 1
                        cur_year += 1
                        print("plus 1 year", time, cur_day, cur_month, cur_year)
            # elif time + n <= 23:
            #     time += 1
    print("time in func 94 =", time)
    if time < 10:
        print("TIME IS LOWER THAN 10")
        time = f"0{time}"
    if cur_day < 10:
        print("DAY IS LOWER THAN 10")
        cur_day = f"0{cur_day}"
    if cur_month < 10:
        print("MONTH IS LOWER THAN 10")
        cur_month = f"0{cur_month}"
    print("CUR DAY =", cur_day)
    date = f"{cur_year}-{cur_month}-{cur_day}"
    return [str(time), date]

def searching_in_dict(dict1, txt):
    # print("dict1 in func =", dict1)
    list = dict1["list"]
    # print("\\ list in func =",list)
    for hour in list:
        dt_txt = hour["dt_txt"]
        print(f'\\ dt_txt in func =', dt_txt)
        print("hour in func =", hour)
        print("txt in func =", txt)
    
        if dt_txt == txt:
            description = hour["weather"][0]["description"]
            temperature = hour["main"]["temp"]
            # print("main =", main)
            print("searching_in_dict =", description, temperature)
            return [description, temperature]
        else:
            continue
            # print("searching_in_dict =", description)
            # return [description]

def searching_time_data(list_json, this_date, this_hours, n):
    txt1 = None
    list_date = this_date.split("-")
    only_hour = int(this_hours.split(":")[0])
    print("only hour =", only_hour)
    find_hour = find_hours(cur_hour = only_hour, cur_day = list_date[-1], cur_month = list_date[1], cur_year = list_date[0], n = n)
    print("find_hour[0] =", find_hour[0])
    if find_hour[0] == "24" or find_hour[0] == "00" or find_hour[0] == "01" or find_hour[0] == "23":
        print("0")
        find_hour[0] = "00"
    elif find_hour[0] == "02" or find_hour[0] == "03" or find_hour[0] == "04":
        print("1")
        find_hour[0] = "03"
    elif find_hour[0] == "05" or find_hour[0] == "06" or find_hour[0] == "07":
        print("2")
        find_hour[0] = "06"
    elif find_hour[0] == "08" or find_hour[0] == "09" or find_hour[0] == "10":
        print("3")
        find_hour[0] = "09"
    elif find_hour[0] == "11" or find_hour[0] == "12" or find_hour[0] == "13":
        print("4")
        find_hour[0] = "12"
    elif find_hour[0] == "14" or find_hour[0] == "15" or find_hour[0] == "16":
        print("5")
        find_hour[0] = "15"
    elif find_hour[0] == "17" or find_hour[0] == "18" or find_hour[0] == "19":
        print("6")
        find_hour[0] = "18"
    elif find_hour[0] == "20" or find_hour[0] == "21" or find_hour[0] == "22":
        print("7")
        find_hour[0] = "21"
    txt1 = f"{find_hour[1]} {find_hour[0]}:00:00"
    print("txt1 in func =", txt1)
    output_dict = searching_in_dict(dict1 = list_json, txt = txt1)
    
    # output_dict = find_description(list = list_json, dt_txt = txt1)
    print("searching_time_data =", output_dict)
    return output_dict
