import tkinter as tk
from tkinter import Entry

# variables
window = tk.Tk()
rus_low = ["а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т", "у", "ф",
           "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я"]
rus_up = ["А", "Б", "В", "Г", "Д", "Е", "Ё", "Ж", "З", "И", "Й", "К", "Л", "М", "Н", "О", "П", "Р", "С", "Т", "У", "Ф",
          "Х", "Ц", "Ч", "Ш", "Щ", "Ъ", "Ы", "Ь", "Э", "Ю", "Я"]
eng_low = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z']
eng_up = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
          'W', 'X', 'Y', 'Z']
symbols = ["%", "*", "?", "@", "#", "$", "~"]
password_el_dict = {'numbers': [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]}
########################################################################################################################
########################################################################################################################
lowercase_letters_check = tk.BooleanVar()
lowercase_letters = tk.Checkbutton(window, text="Включать строчные буквы", bg="#d2d4d3", activebackground="#d2d4d3",
                                   variable=lowercase_letters_check, onvalue=True, offvalue=False)

uppercase_letters_check = tk.BooleanVar()
uppercase_letters = tk.Checkbutton(window, text="Включать прописные буквы", bg="#d2d4d3", activebackground="#d2d4d3",
                                   variable=uppercase_letters_check, onvalue=True, offvalue=False)

to_include_eng_check = tk.BooleanVar()
to_include_eng = tk.Checkbutton(window, text="Включать Латиницу", bg="#d2d4d3", activebackground="#d2d4d3",
                                variable=to_include_eng_check, onvalue=True, offvalue=False, state='disabled')

to_include_rus_check = tk.BooleanVar()
to_include_rus = tk.Checkbutton(window, text="Включать Кириллицу", bg="#d2d4d3", activebackground="#d2d4d3",
                                variable=to_include_rus_check, onvalue=True, offvalue=False, state='disabled')

spec_symbols_check = tk.BooleanVar()
spec_symbols = tk.Checkbutton(window, text="Включать спец. символы", bg="#d2d4d3", activebackground="#d2d4d3",
                              variable=spec_symbols_check, onvalue=True, offvalue=False)

to_not_include_numbers_check = tk.BooleanVar()
to_not_include_numbers = tk.Checkbutton(window, text="Не включать цифры", bg="#d2d4d3", activebackground="#d2d4d3",
                                        variable=to_not_include_numbers_check, onvalue=True, offvalue=False)

to_not_repeat_el_check = tk.BooleanVar()
to_not_repeat_el = tk.Checkbutton(window, text="Не повторять элементы", bg="#d2d4d3", activebackground="#d2d4d3",
                                  variable=to_not_repeat_el_check, onvalue=True, offvalue=False)
########################################################################################################################
########################################################################################################################
settings_label = tk.Label(window, text="Настройки:", bg="#CFCFCF", relief=tk.RAISED)
amount_of_symbols_label = tk.Label(window, text="Кол-во символов:", bg="#d2d4d3", relief=tk.FLAT)
result_label = tk.Label(window, text="Результат:", bg="#d2d4d3", relief=tk.GROOVE)
result_entry: Entry = tk.Entry(window, bg="#d2d4d3", width=20, state='normal')
cannot_be_generated_label = tk.Label(window, text='Генерация невозможна', bg="#d2d4d3", fg='red')
error_label_symbols = tk.Label(window, text="Кол-во символов должно быть \nцелым числом, большим 4", bg="#d2d4d3",
                               fg="red")
amount_of_symbols = tk.Entry(window, bg="#d2d4d3", width=4)
gen_btn = tk.Button(window, text="Сгенерировать", bg="#d2d4d3", activebackground="#d2d4d3")
# visual
window.title("Password Generator")
window.geometry("300x400+600+100")
window.resizable(False, False)
window.config(bg="#d2d4d3")
icon = tk.PhotoImage(file='pass_gen_icon.png')
window.iconphoto(False, icon)
# running
settings_label.pack()
to_include_eng.place(relx=.5, rely=.1, anchor="center")
to_include_rus.place(relx=.514, rely=.15, anchor="center")
to_not_include_numbers.place(relx=.502, rely=.2, anchor="center")
lowercase_letters.place(relx=.563, rely=.25, anchor="center")
uppercase_letters.place(relx=.575, rely=.3, anchor="center")
spec_symbols.place(relx=.55, rely=.35, anchor="center")
to_not_repeat_el.place(relx=.535, rely=.4, anchor="center")
amount_of_symbols_label.place(relx=.514, rely=.45, anchor="center")
amount_of_symbols.place(relx=.514, rely=.5, anchor="center")
gen_btn.place(relx=.514, rely=.60, anchor="center")
result_label.place(relx=.514, rely=.8, anchor="center")
result_entry.place(relx=.514, rely=.87, anchor="center")

