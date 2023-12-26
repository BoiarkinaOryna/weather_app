import customtkinter
import modules.path_to_file as path
from PIL import Image
import subprocess
import modules.functions as func
import registration as reg

off_app = customtkinter.CTk()
off_app.resizable(height= False, width= False)
off_app.config(bg = "#5DA7B1")

off_app.geometry("460x645x573x643")
off_app.title("Особистий кабінет")

# print(text_surname)
    
font_h = customtkinter.CTkFont(
    family = "Roboto Slab",
    size = 30
)

text_h = customtkinter.CTkLabel(
    master = off_app,
    text_color = "white",
    bg_color = "#5DA7B1",
    text = "Особистий кабінет",
    font = font_h
)
text_h.place(x = 38, y = 42)

font_p = customtkinter.CTkFont(
    family = "Roboto Slab",
    size = 20
)

font_info = customtkinter.CTkFont(
    family = "Roboto Slab",
    size = 28,
    underline = True
    
)

text_p1 = customtkinter.CTkLabel(
    master = off_app,
    padx = 5,
    pady = 2,
    text_color = "white",
    bg_color = "#5DA7B1",
    text = "Країна:",
    font = font_p
)
text_p1.place(x = 46, y = 108)

user_country = customtkinter.CTkLabel(
    master = off_app,
    text_color = "white",
    bg_color = "#5DA7B1",
    text = func.select(surname = reg.text_surname, name = reg.text_name)[0][0],
    font = font_info
)
user_country.place(x = 119, y = 157)

text_p2 = customtkinter.CTkLabel(
    master = off_app,
    text_color = "white",
    bg_color = "#5DA7B1",
    text = "Місто:",
    font = font_p
)
text_p2.place(x = 46, y = 207)

user_city = customtkinter.CTkLabel(
    master = off_app,
    text_color = "white",
    bg_color = "#5DA7B1",
    text = func.select(surname = reg.text_surname, name = reg.text_name)[0][1],
    font = font_info
)
user_city.place(x = 121, y = 256)

text_p3 = customtkinter.CTkLabel(
    master = off_app,
    text_color = "white",
    bg_color = "#5DA7B1",
    text = "Ім'я:",
    font = font_p
)
text_p3.place(x = 46, y = 306)

user_name = customtkinter.CTkLabel(
    master = off_app,
    text_color = "white",
    bg_color = "#5DA7B1",
    text = func.select(surname = reg.text_surname, name = reg.text_name)[0][2],
    font = font_info
)
user_name.place(x = 121, y = 352)

text_p4 = customtkinter.CTkLabel(
    master = off_app,
    text_color = "white",
    bg_color = "#5DA7B1",
    text = "Прізвище:",
    font = font_p
)
text_p4.place(x = 46, y = 405)

user_surname = customtkinter.CTkLabel(
    master = off_app,
    text_color = "white",
    bg_color = "#5DA7B1",
    text = func.select(surname = reg.text_surname, name = reg.text_name)[0][3],
    font = font_info
    
)
user_surname.place(x = 119, y = 455)

def button_clicked():
    # subprocess.run(["python", "main.py"])
    off_app.destroy()
      
button = customtkinter.CTkButton(
    master = off_app,
    width = 218,
    height = 46,
    border_width = 3, 
    border_color = "white",
    bg_color = "#5DA7B1",
    fg_color = "#1f333c",
    text = "Перейти до додатку",
    corner_radius = 50,
    command = button_clicked
)
button.place(x = 119, y = 546)

btn_img = customtkinter.CTkImage(
    light_image = Image.open(path.path_to_file() + "\\exit.png"),
    size = (28, 29)
)

def exit():
    # print("Button  clicked!")
    # reg = open("registration.py", mode = "w")
    # run_reg = exec(open("registration.py").read)
    off_app.destroy()
    reg.text_name = None
    reg.text_surname = None
    # subprocess.run(["python", "registration.py"])
    subprocess.run(["python", "office.py"])

label = customtkinter.CTkLabel(
    master = off_app,
    text = "Вихід",
    font = ("Roboto Slab", 12),
    text_color = "white",
    bg_color = "#5DA7B1"
)
label.place(x = 370, y = 26)

img_button = customtkinter.CTkButton(
    master = off_app,
    text = "",
    bg_color = "#5DA7B1",
    fg_color = "#5DA7B1",
    hover_color= "#5DA7B1",
    command = exit,
    width = 40,
    height = 40,
    image = btn_img
)

img_button.place(x = 409 , y = 20)

off_app.mainloop()