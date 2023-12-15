from PIL import Image
import modules.path_to_file as m_path
import customtkinter 

# def set_day_night(list_json, data_time):
#     list_json
#     timestamp = (date_time -"0001-01-01T00:00:00Z) * 86400

def find_images(app1, description, width, height, time = "day"):
    if time == "day":
    
        if description == "легкий дощ":
            image = "drizzle_412695.png"
        elif description == "сніг" or description == "легкий сніг":
            image = "snowy_2412768.png"
        elif description == "дощ":
            image = "rainy_2412747.png"
        elif description == "хмарно" or description == "рвані хмари":
            image = "day_clouds.png"
        elif description == "ясно":
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
            image = None
    
    image_weather = customtkinter.CTkImage(
        light_image = Image.open(m_path.path_to_file() + f"\\{image}"),
        size = (width, height)
    )
    image_weather_lable = customtkinter.CTkLabel(
        master = app1,
        bg_color = "#5DA7B1",
        text = "",
        image = image_weather
    )
    return image_weather_lable