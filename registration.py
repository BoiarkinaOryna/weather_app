import customtkinter
import sys
import sqlite3
app = customtkinter.CTk()
app.resizable(width= False, height= False)
app.config(
    bg = "#5DA7B1",
    borderwidth = 5,
    )


app.geometry("460x645x643x62")
app.title("Реєстрація користувача")

font_h = customtkinter.CTkFont(
    family = "Arial",
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
text_p1.place(x = 20, y = 150)

text_p2 = customtkinter.CTkLabel(
    master = app,
    text_color = "white",
    bg_color = "#5DA7B1",
    text = "Місто:",
     font = ("Roboto Slab", 22)
)
text_p2.place(x = 20, y = 250)

text_p3 = customtkinter.CTkLabel(
    master = app,
    text_color = "white",
    bg_color = "#5DA7B1",
    text = "Ім'я:",
    font = ("Roboto Slab", 22)
)
text_p3.place(x = 20, y = 350)

text_p4 = customtkinter.CTkLabel(
    master = app,
    text_color = "white",
    bg_color = "#5DA7B1",
    text = "Прізвище:",
    font = ("Roboto Slab", 22)
)
text_p4.place(x= 20, y = 450)

entry1 = customtkinter.CTkEntry(
    master = app,
    width = 218,
    height = 46,
    bg_color = "#5DA7B1",
    fg_color = "#096C82",
    border_width = 3,
    border_color = "white",
    corner_radius = 50,
)
entry1.place(x = 20, y = 200)

entry2 = customtkinter.CTkEntry(
    master = app,
    width = 218,
    height = 46,
    bg_color = "#5DA7B1",
    fg_color = "#096C82",
    border_width = 3,
    border_color = "white",
    corner_radius = 50,
    
)
entry2.place(x = 20, y = 300)


entry3 = customtkinter.CTkEntry(
    master = app,
    width = 295,
    height = 46,
    bg_color = "#5DA7B1",
    fg_color = "#096C82",
    border_width = 3,
    border_color= "white",
    corner_radius = 50
)

entry3.place(x = 20, y = 400)

entry4 = customtkinter.CTkEntry(
    master = app,
    width = 295,
    height = 46,
    bg_color = "#5DA7B1",
    fg_color = "#096C82",
    border_width = 3,
    border_color = "white",
    corner_radius = 50
)

entry4.place(x = 20, y = 500)
    
    
def save():
    db = sqlite3.connect("database.db")
    cursor = db.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS Users (country TEXT, city TEXT, name TEXT, surname TEXT)")
    
    text_country = entry1.get()
    text_city = entry2.get()
    text_name = entry3.get()
    text_surname = entry4.get()
    print(text_country)
    cursor.execute(f"INSERT INTO Users (country, city, name, surname) VALUES (?, ?, ?, ?)", (text_country, text_city, text_name, text_surname))
    
    db.commit()
    db.close()
    print("1")
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
button.place(x = 119, y = 596)

app.mainloop()