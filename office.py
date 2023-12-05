import customtkinter
import sqlite3
import registration as reg
import path_to_file as path

app = customtkinter.CTk()
app.resizable(height= False, width= False)
app.config(bg = "#5DA7B1")

app.geometry("460x645x573x643")
app.title("Особистий кабінет")

print(reg.text_surname)

db = sqlite3.connect("database.db")
cursor = db.cursor()

def select(surname: str, name: str):
    cursor.execute('SELECT * FROM Users WHERE surname = ?', [surname])
    cursor.execute('SELECT * FROM Users WHERE name = ?', [name])
    return cursor.fetchall()
    
font_h = customtkinter.CTkFont(
    family = "Roboto Slab",
    size = 30
)

text_h = customtkinter.CTkLabel(
    master = app,
    text_color = "white",
    bg_color = "#5DA7B1",
    text = "Особистий кабінет",
    font = font_h
)
text_h.place(x = 230, y = 50, anchor = customtkinter.CENTER)

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
    master = app,
    padx = 5,
    pady = 2,
    text_color = "white",
    bg_color = "#5DA7B1",
    text = "Країна:",
    font = font_p
)
text_p1.place(x = 46, y = 108)

user_country = customtkinter.CTkLabel(
    master = app,
    text_color = "white",
    bg_color = "#5DA7B1",
    text = select(surname = reg.text_surname, name = reg.text_name)[0][0],
    font = font_info
)
user_country.place(x = 119, y = 157)

text_p2 = customtkinter.CTkLabel(
    master = app,
    text_color = "white",
    bg_color = "#5DA7B1",
    text = "Місто:",
    font = font_p
)
text_p2.place(x = 46, y = 207)

user_city = customtkinter.CTkLabel(
    master = app,
    text_color = "white",
    bg_color = "#5DA7B1",
    text = select(surname = reg.text_surname, name = reg.text_name)[0][1],
    font = font_info
)
user_city.place(x = 121, y = 256)

text_p3 = customtkinter.CTkLabel(
    master = app,
    text_color = "white",
    bg_color = "#5DA7B1",
    text = "Ім'я:",
    font = font_p
)
text_p3.place(x = 46, y = 306)

user_name = customtkinter.CTkLabel(
    master = app,
    text_color = "white",
    bg_color = "#5DA7B1",
    text = select(surname = reg.text_surname, name = reg.text_name)[0][2],
    font = font_info
)
user_name.place(x = 121, y = 352)

text_p4 = customtkinter.CTkLabel(
    master = app,
    text_color = "white",
    bg_color = "#5DA7B1",
    text = "Прізвище:",
    font = font_p
)
text_p4.place(x = 46, y = 405)

user_surname = customtkinter.CTkLabel(
    master = app,
    text_color = "white",
    bg_color = "#5DA7B1",
    text = select(surname = reg.text_surname, name = reg.text_name)[0][3],
    font = font_info
    
)
user_surname.place(x = 119, y = 455)

button = customtkinter.CTkButton(
    master = app,
    width = 218,
    height = 46,
    border_width = 3, 
    border_color = "white",
    bg_color = "#5DA7B1",
    fg_color = "#096C82",
    text = "Перейти до додатку",
    corner_radius = 50,
    command = app.destroy
)
button.place(x = 119, y = 546)

db.commit()
db.close()
app.mainloop()