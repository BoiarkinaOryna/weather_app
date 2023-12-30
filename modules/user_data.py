# import sqlite3
# import registration as reg

def write_user_data(text_country1, text_city1, text_name1, text_surname1):
    # global text_country, text_city, text_name, text_surname
    text_country = text_country1
    text_city = text_city1
    text_name = text_name1
    text_surname = text_surname1
    print("text_name =", text_name, "text_surname = ", text_surname)
    if text_surname == text_surname1:
        print("writing data in user data successfully")

text_country = None
text_city = None
text_name = None
text_surname = None

print("IN USER DATA text_name =", text_name, "text_surname = ", text_surname)