from datetime import date
from tkinter import Tk, Label, Entry, Button, StringVar, END, Frame
from tkcalendar import Calendar

class AgeCalculator:
    def __init__(self, master):
        self.master = master
        master.title("Age Calculator")
        master.configure(bg='light blue')  # Set background color for the main window

        # Use a Frame to group widgets and set a background color
        main_frame = Frame(master, bg='white', padx=10, pady=10)
        main_frame.grid(row=0, column=0, padx=10, pady=10)

        self.birth_date_label = Label(main_frame, text="Enter Birth Date (MM/DD/YYYY):", bg='white', fg='black')
        self.birth_date_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.birth_date_entry = Entry(main_frame, bg='light yellow')
        self.birth_date_entry.grid(row=0, column=1, padx=10, pady=10)

        self.calendar_button = Button(main_frame, text="Select Date", command=self.open_calendar, bg='light green')
        self.calendar_button.grid(row=0, column=2, padx=5, pady=10)

        self.result_label_var = StringVar()
        self.result_label = Label(main_frame, textvariable=self.result_label_var, bg='white', fg='blue')
        self.result_label.grid(row=1, column=0, columnspan=3, pady=10)

        self.calculate_button = Button(main_frame, text="Calculate Age", command=self.calculate_age, bg='orange')
        self.calculate_button.grid(row=2, column=0, columnspan=3, pady=10)

        self.calendar_window = None
        self.selected_date = None

    def open_calendar(self):
        self.calendar_window = Tk()
        self.calendar_window.title("Select Birth Date")
        cal = Calendar(self.calendar_window, selectmode='day', date_pattern='mm/dd/yyyy')
        cal.grid(row=0, column=0, padx=10, pady=10)
        select_button = Button(self.calendar_window, text="Select", command=lambda: self.set_date_from_calendar(cal.get_date()), bg='lightgray')
        select_button.grid(row=1, column=0, pady=5)
        self.calendar_window.mainloop()

    def set_date_from_calendar(self, selected_date_str):
        self.birth_date_entry.delete(0, END)
        self.birth_date_entry.insert(0, selected_date_str)
        self.calendar_window.destroy()

    def calculate_age(self):
        birth_date_str = self.birth_date_entry.get()
        try:
            birth_month, birth_day, birth_year = map(int, birth_date_str.split('/'))
            birth_date = date(birth_year, birth_month, birth_day)
            today = date.today()
            age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
            self.result_label_var.set(f"You are {age} years old")
        except ValueError:
            self.result_label_var.set("Invalid date format. Please use MM/DD/YYYY.")

if __name__ == "__main__":
    root = Tk()
    app = AgeCalculator(root)
    root.mainloop()