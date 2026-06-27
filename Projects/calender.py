#######   Welcome to Date converter   #######

import tkinter as tk
import jdatetime
import hijri_converter
from datetime import datetime

# Defining colors for the user interface
BG_COLOR = "#f0f0f0"
FG_COLOR = "#333"

# Function for displaying today's date in three different formats
def show_today_date():
    today_miladi = datetime.now()
    today_shamsi = jdatetime.date.fromgregorian(date=today_miladi)
    today_qamari = hijri_converter.convert.Gregorian(today_miladi.year, today_miladi.month, today_miladi.day).to_hijri()

    lbl_shamsi.config(text=f"شمسی: {today_shamsi.strftime('%Y/%m/%d')}")
    lbl_miladi.config(text=f"میلادی: {today_miladi.strftime('%Y/%m/%d')}")
    lbl_qamari.config(text=f"قمری: {today_qamari.year}/{today_qamari.month}/{today_qamari.day}")

# Function for converting dates
def convert_date():
    try:
        input_date = entry_date.get()
        date_format = date_format_var.get()

        if date_format == "miladi":
            year, month, day = map(int, input_date.split('/'))
            date_miladi = datetime(year, month, day)
            date_shamsi = jdatetime.date.fromgregorian(date=date_miladi)
            date_qamari = hijri_converter.convert.Gregorian(year, month, day).to_hijri()
        elif date_format == "shamsi":
            year, month, day = map(int, input_date.split('/'))
            date_shamsi = jdatetime.date(year, month, day)
            date_miladi = date_shamsi.togregorian()
            date_qamari = hijri_converter.convert.Gregorian(date_miladi.year, date_miladi.month, date_miladi.day).to_hijri()
        elif date_format == "qamari":
            year, month, day = map(int, input_date.split('/'))
            date_qamari = hijri_converter.convert.Hijri(year, month, day)
            date_miladi = date_qamari.to_gregorian()
            date_shamsi = jdatetime.date.fromgregorian(date=date_miladi)

        lbl_convert_shamsi.config(text=f"شمسی: {date_shamsi.strftime('%Y/%m/%d')}")
        lbl_convert_miladi.config(text=f"میلادی: {date_miladi.strftime('%Y/%m/%d')}")
        lbl_convert_qamari.config(text=f"قمری: {date_qamari.year}/{date_qamari.month}/{date_qamari.day}")
    except ValueError:
        lbl_convert_shamsi.config(text="خطا: فرمت تاریخ نادرست است")
        lbl_convert_miladi.config(text="")
        lbl_convert_qamari.config(text="")

# Function for creating the main window of the application
app = tk.Tk()
app.title("تقویم چندگانه")
app.geometry("450x500")
app.configure(bg=BG_COLOR)

# Creating widgets and placing them in the window
lbl_shamsi = tk.Label(app, text="شمسی: ", bg=BG_COLOR, fg=FG_COLOR)
lbl_shamsi.pack()

lbl_miladi = tk.Label(app, text="میلادی: ", bg=BG_COLOR, fg=FG_COLOR)
lbl_miladi.pack()

lbl_qamari = tk.Label(app, text="قمری: ", bg=BG_COLOR, fg=FG_COLOR)
lbl_qamari.pack()

btn_show = tk.Button(app, text="نمایش تاریخ امروز", command=show_today_date)
btn_show.pack()

lbl_date_format = tk.Label(app, text="فرمت تاریخ برای تبدیل: YYYY/MM/DD", bg=BG_COLOR, fg=FG_COLOR)
lbl_date_format.pack()

date_format_var = tk.StringVar(app)
date_format_var.set("miladi") # Default value
date_format_menu = tk.OptionMenu(app, date_format_var, "miladi", "shamsi", "qamari")
date_format_menu.pack()

entry_date = tk.Entry(app)
entry_date.pack()

btn_convert = tk.Button(app, text="تبدیل تاریخ", command=convert_date)
btn_convert.pack()

lbl_convert_shamsi = tk.Label(app, text="تبدیل شده به شمسی: ", bg=BG_COLOR, fg=FG_COLOR)
lbl_convert_shamsi.pack()

lbl_convert_miladi = tk.Label(app, text="تبدیل شده به میلادی: ", bg=BG_COLOR, fg=FG_COLOR)
lbl_convert_miladi.pack()

lbl_convert_qamari = tk.Label(app, text="تبدیل شده به قمری: ", bg=BG_COLOR, fg=FG_COLOR)
lbl_convert_qamari.pack()

# Start of the main loop of the program
app.mainloop()

print("Have a great day with the Date converter!")