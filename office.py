import customtkinter
import sqlite3
# import regestration

app = customtkinter.CTk()
app.config(bg = "#5DA7B1")
width = app.winfo_screenwidth()
height = app.winfo_screenheight()

app.geometry(f"460x645x{width}x{height}")
app.title("Особистий кабінет")

db = sqlite3.connect("database.db")
cursor = db.cursor()

def select(name_column: str, name_table: str, surname: str):
    cursor.execute(f'SELECT {name_column} FROM {name_table} WHERE surname = {surname}')
    print(cursor.fetchall())
    text = cursor.fetchall()
    db.commit()
    print(text)
    
    return text


font_h = customtkinter.CTkFont(
    family = "Arial",
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
    family = "Arial",
    size = 20
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
text_p1.place(x = 20, y = 150)

text_p2 = customtkinter.CTkLabel(
    master = app,
    text_color = "white",
    bg_color = "#5DA7B1",
    text = "Місто:",
    font = font_p
)
text_p2.place(x = 20, y = 250)

text_p3 = customtkinter.CTkLabel(
    master = app,
    text_color = "white",
    bg_color = "#5DA7B1",
    text = "Ім'я:",
    font = font_p
)
text_p3.place(x = 20, y = 350)

user_name = customtkinter.CTkLabel(
    master = app,
    text_color = "white",
    bg_color = "#5DA7B1",
    text = select(name_column = "name", name_table = "Users", surname = "surname"),
    font = font_p
)
user_name.place(x = 121, y = 352)

text_p4 = customtkinter.CTkLabel(
    master = app,
    text_color = "white",
    bg_color = "#5DA7B1",
    text = "Прізвище:",
    font = font_p
)
text_p4.place(x= 20, y = 450)

db.close()
app.mainloop()