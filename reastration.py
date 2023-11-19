import customtkinter
import sys
from PyQt5 import Qt
app = customtkinter.CTk()
app.config(bg = "#5DA7B1")
width = app.winfo_screenwidth()
height = app.winfo_screenheight()
# print(width, height)
# print(width / 2, height / 2)
# print((width / 2) - (460 / 2), (height / 2) - (645 / 2))
app.geometry(f"460 x 645 x {(width / 2) - (460 / 2)} x {(height / 2) - (645 / 2)}")
app.title("Реєстрація користувача")

app.mainloop()