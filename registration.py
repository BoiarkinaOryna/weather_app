import customtkinter
import sys
import sqlite3
app = customtkinter.CTk()
app.resizable(width= False, height= False)
app.config(
    bg = "#5DA7B1",
    borderwidth = 5,
    )
text_country = None
text_city = None
text_name = None
text_surname = None

app.geometry("460x645x643x62")
app.title("Реєстрація користувача")

font_h = customtkinter.CTkFont(
    family = "Roboto Slab",
    weight = "bold",
    size = 28
)

text_h = customtkinter.CTkLabel(
    master = app,
    width = 87,
    height = 31,
    text_color = "white",
    bg_color = "#5DA7B1",
    text = "Реєстрація користувача",
    font = font_h
)
text_h.place(x = 38, y = 42)

text_p1 = customtkinter.CTkLabel(
    master = app,
    # padx = 5,
    # pady = 2,
    text_color = "white",
    bg_color = "#5DA7B1",
    text = "Країна:",
    font = ("Roboto Slab", 22)
)
text_p1.place(x = 46, y = 108)

text_p2 = customtkinter.CTkLabel(
    master = app,
    text_color = "white",
    bg_color = "#5DA7B1",
    text = "Місто:",
    font = ("Roboto Slab", 22)
)
text_p2.place(x = 46, y = 207)

text_p3 = customtkinter.CTkLabel(
    master = app,
    text_color = "white",
    bg_color = "#5DA7B1",
    text = "Ім'я:",
    font = ("Roboto Slab", 22)
)
text_p3.place(x = 46, y = 306)

text_p4 = customtkinter.CTkLabel(
    master = app,
    text_color = "white",
    bg_color = "#5DA7B1",
    text = "Прізвище:",
    font = ("Roboto Slab", 22)
)
text_p4.place(x = 46, y = 405)

# text_entry = "your data in English"

entry1 = customtkinter.CTkEntry(
    master = app,
    width = 218,
    height = 46,
    bg_color = "#5DA7B1",
    fg_color = "#096C82",
    border_width = 3,
    border_color = "white",
    corner_radius = 50,
    # textvariable = text_entry
)
entry1.place(x = 38, y = 150)

entry2 = customtkinter.CTkEntry(
    master = app,
    width = 218,
    height = 46,
    bg_color = "#5DA7B1",
    fg_color = "#096C82",
    border_width = 3,
    border_color = "white",
    corner_radius = 50,
    # textvariable = text_entry
)
entry2.place(x = 38, y = 249)


entry3 = customtkinter.CTkEntry(
    master = app,
    width = 295,
    height = 46,
    bg_color = "#5DA7B1",
    fg_color = "#096C82",
    border_width = 3,
    border_color= "white",
    corner_radius = 50,
    # textvariable = text_entry
)

entry3.place(x = 38, y = 348)

entry4 = customtkinter.CTkEntry(
    master = app,
    width = 295,
    height = 46,
    bg_color = "#5DA7B1",
    fg_color = "#096C82",
    border_width = 3,
    border_color = "white",
    corner_radius = 50,
    # textvariable = text_entry
)

entry4.place(x = 38, y = 447)
    
    
def save():
    global text_country, text_city, text_name, text_surname
    db = sqlite3.connect("database.db")
    cursor = db.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS Users (country TEXT, city TEXT, name TEXT, surname TEXT)")
    
    text_country = entry1.get()
    text_city = entry2.get()
    text_name = entry3.get()
    text_surname = entry4.get()
    cursor.execute("INSERT INTO Users (country, city, name, surname) VALUES (?, ?, ?, ?)", (text_country, text_city, text_name, text_surname))
    
    db.commit()
    db.close()
    app.destroy()
    

button = customtkinter.CTkButton(
    master = app,
    width = 218,
    height = 46,
    border_width = 3, 
    border_color = "white",
    bg_color = "#5DA7B1",
    fg_color = "#096C82",
    text = "Зберегти",
    corner_radius = 50,
    command = save
)
button.place(x = 119, y = 546)

app.mainloop()