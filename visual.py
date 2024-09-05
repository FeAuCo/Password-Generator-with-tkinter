import tkinter as tk

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
lowercase_letters = tk.Checkbutton(window, text="Include lowercase letters", bg="#d2d4d3", activebackground="#d2d4d3",
                                   variable=lowercase_letters_check, onvalue=True, offvalue=False)

uppercase_letters_check = tk.BooleanVar()
uppercase_letters = tk.Checkbutton(window, text="Include uppercase letters", bg="#d2d4d3", activebackground="#d2d4d3",
                                   variable=uppercase_letters_check, onvalue=True, offvalue=False)

to_include_eng_check = tk.BooleanVar()
to_include_eng = tk.Checkbutton(window, text="Include Latin", bg="#d2d4d3", activebackground="#d2d4d3",
                                variable=to_include_eng_check, onvalue=True, offvalue=False, state='disabled')

to_include_rus_check = tk.BooleanVar()
to_include_rus = tk.Checkbutton(window, text="Include Cyrillic", bg="#d2d4d3", activebackground="#d2d4d3",
                                variable=to_include_rus_check, onvalue=True, offvalue=False, state='disabled')

spec_symbols_check = tk.BooleanVar()
spec_symbols = tk.Checkbutton(window, text="Include spec. symbols", bg="#d2d4d3", activebackground="#d2d4d3",
                              variable=spec_symbols_check, onvalue=True, offvalue=False)

to_not_include_numbers_check = tk.BooleanVar()
to_not_include_numbers = tk.Checkbutton(window, text="Not include numbers", bg="#d2d4d3", activebackground="#d2d4d3",
                                        variable=to_not_include_numbers_check, onvalue=True, offvalue=False)

to_not_repeat_el_check = tk.BooleanVar()
to_not_repeat_el = tk.Checkbutton(window, text="Not repeat elements", bg="#d2d4d3", activebackground="#d2d4d3",
                                  variable=to_not_repeat_el_check, onvalue=True, offvalue=False)
########################################################################################################################
########################################################################################################################
settings_label = tk.Label(window, text="Settings:", bg="#CFCFCF", relief=tk.RAISED)
amount_of_symbols_label = tk.Label(window, text="Amount of symbols:", bg="#d2d4d3", relief=tk.FLAT)
result_label = tk.Label(window, text="Result:", bg="#d2d4d3", relief=tk.GROOVE)
result_entry: tk.Entry = tk.Entry(window, bg="#d2d4d3", width=20, state='normal')
cannot_be_generated_label = tk.Label(window, text='Generation is impossible', bg="#d2d4d3", fg='red')
error_label_symbols = tk.Label(window, text="Amount of symbols must be \nInteger which is greater than 4", bg="#d2d4d3",
                               fg="red")
amount_of_symbols = tk.Entry(window, bg="#d2d4d3", width=4)
gen_btn = tk.Button(window, text="Generate", bg="#d2d4d3", activebackground="#d2d4d3")
# visual
window.title("Password Generator")
window.geometry("300x400+600+100")
window.resizable(False, False)
window.config(bg="#d2d4d3")
icon = tk.PhotoImage(file='pass_gen_icon.png')
window.iconphoto(False, icon)
# running
settings_label.pack()
to_include_eng.place(x=130, y=40, anchor="center")
to_include_rus.place(x=135, y=60, anchor="center")
to_not_include_numbers.place(x=152, y=80, anchor="center")
lowercase_letters.place(x=160, y=100, anchor="center")
uppercase_letters.place(x=162, y=120, anchor="center")
spec_symbols.place(x=155, y=140, anchor="center")
to_not_repeat_el.place(x=150, y=160, anchor="center")

amount_of_symbols_label.place(x=145, y=195, anchor="center")
amount_of_symbols.place(x=145, y=215, anchor="center")
gen_btn.place(x=145, y=250, anchor="center")
result_label.place(x=145, y=310, anchor="center")
result_entry.place(x=145, y=335, anchor="center")
