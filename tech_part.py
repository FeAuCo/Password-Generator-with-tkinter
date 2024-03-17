import tkinter as tk
import random
from visual import window, rus_low, rus_up, eng_low, eng_up, symbols, password_el_dict, lowercase_letters_check, \
    lowercase_letters, uppercase_letters_check, uppercase_letters, to_include_eng_check, to_include_eng, \
    to_include_rus_check, to_include_rus, spec_symbols_check, spec_symbols, to_not_include_numbers_check, \
    to_not_include_numbers, error_label_symbols, amount_of_symbols, gen_btn, to_not_repeat_el_check, \
    result_entry, cannot_be_generated_label


# button's funcs
def act_low():
    to_include_eng['state'] = tk.NORMAL
    to_include_rus['state'] = tk.NORMAL
    if lowercase_letters_check.get() is True:
        if to_include_eng_check.get() is True:
            password_el_dict.update({'eng_low_d': eng_low})
        elif to_include_eng_check.get() is False:
            try:
                password_el_dict.pop('eng_low_d')
            except KeyError:
                pass
        if to_include_rus_check.get() is True:
            password_el_dict.update({'rus_low_d': rus_low})
        elif to_include_rus_check.get() is False:
            try:
                password_el_dict.pop('rus_low_d')
            except KeyError:
                pass
    else:
        try:
            password_el_dict.pop('rus_low_d')
        except KeyError:
            pass
        try:
            password_el_dict.pop('eng_low_d')
        except KeyError:
            pass
        if uppercase_letters_check.get() is False:
            to_include_eng['state'] = tk.DISABLED
            to_include_rus['state'] = tk.DISABLED


def act_up():
    to_include_eng['state'] = tk.NORMAL
    to_include_rus['state'] = tk.NORMAL
    if uppercase_letters_check.get() is True:
        if to_include_eng_check.get() is True:
            password_el_dict.update({'eng_up_d': eng_up})
        elif to_include_eng_check.get() is False:
            try:
                password_el_dict.pop('eng_up_d')
            except KeyError:
                pass
        if to_include_rus_check.get() is True:
            password_el_dict.update({'rus_up_d': rus_up})
        elif to_include_rus_check.get() is False:
            try:
                password_el_dict.pop('rus_up_d')
            except KeyError:
                pass
    else:
        try:
            password_el_dict.pop('rus_up_d')
        except KeyError:
            pass
        try:
            password_el_dict.pop('eng_up_d')
        except KeyError:
            pass
        if lowercase_letters_check.get() is False:
            to_include_eng['state'] = tk.DISABLED
            to_include_rus['state'] = tk.DISABLED


def no_numbers():
    if to_not_include_numbers_check.get() is True:
        try:
            password_el_dict.pop('numbers')
        except KeyError:
            pass
    else:
        password_el_dict.update({'numbers': [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]})


def act_symbols():
    if spec_symbols_check.get() is True:
        password_el_dict.update({'symbols_d': symbols})
    else:
        password_el_dict.pop('symbols_d')


# checks
def check_amount_of_symbols():
    x_amount_of_symbols = amount_of_symbols.get()
    try:
        x_amount_of_symbols = int(x_amount_of_symbols)
    except ValueError:
        error_label_symbols.place(relx=.54, rely=.7, anchor="center")
        amount_of_symbols.delete(0, tk.END)
        return False
    else:
        if x_amount_of_symbols <= 4:
            error_label_symbols.place(relx=.54, rely=.7, anchor="center")
            amount_of_symbols.delete(0, tk.END)
            return False
    return True


def gen_alg():
    global result_list
    result_list = []
    to_not_repeat_el_check_list = []
    list_with_listed_dict_values = [value_l for value_l in password_el_dict.values()]
    for i in range(int(amount_of_symbols.get())):
        list_to_choose_el_for_password = list_with_listed_dict_values[
            random.randint(0, len(list_with_listed_dict_values) - 1)]
        el_for_password = list_to_choose_el_for_password[random.randint(0, len(list_to_choose_el_for_password) - 1)]
        if to_not_repeat_el_check.get() is False:
            result_list.append(el_for_password)
            to_not_repeat_el_check_list.append(el_for_password)
        elif to_not_repeat_el_check.get() is True and el_for_password not in to_not_repeat_el_check_list:
            result_list.append(el_for_password)
            to_not_repeat_el_check_list.append(el_for_password)
        elif to_not_repeat_el_check.get() is True and el_for_password in to_not_repeat_el_check_list:
            while el_for_password in to_not_repeat_el_check_list:
                list_to_choose_el_for_password = list_with_listed_dict_values[
                    random.randint(0, len(list_with_listed_dict_values) - 1)]
                el_for_password = list_to_choose_el_for_password[
                    random.randint(0, len(list_to_choose_el_for_password) - 1)]
            result_list.append(el_for_password)
            to_not_repeat_el_check_list.append(el_for_password)


# validating
def too_big_amount_of_symbols():
    if to_not_repeat_el_check.get():
        if to_not_include_numbers_check.get():
            x_amount_of_symbols=0
        else:
            x_amount_of_symbols = 10
        if spec_symbols_check.get():
            x_amount_of_symbols+=7
        if uppercase_letters_check.get():
            if to_include_eng_check.get():
                x_amount_of_symbols += 26
            if to_include_rus_check.get():
                x_amount_of_symbols += 33
        if lowercase_letters_check.get():
            if to_include_eng_check.get():
                x_amount_of_symbols += 26
            if to_include_rus_check.get():
                x_amount_of_symbols += 33
        if int(amount_of_symbols.get()) > x_amount_of_symbols:
            cannot_be_generated_label.place(relx=.54, rely=.7, anchor="center")
            return False
    return True


def cannot_be_generated():
    if to_not_include_numbers_check.get() is True and spec_symbols_check.get() is False and (
            (uppercase_letters_check.get() is True or lowercase_letters_check.get() is True) and (
            to_include_eng_check.get() is False and to_include_rus_check.get() is False) or (
                    uppercase_letters_check.get() is False and lowercase_letters_check.get() is False)):
        cannot_be_generated_label.place(relx=.54, rely=.7, anchor="center")
        return False
    return True


def gen_end():
    result_entry.delete(0, 'end')
    password = ''
    if cannot_be_generated():
        if cannot_be_generated_label.winfo_exists():
            cannot_be_generated_label.place_forget()
        if check_amount_of_symbols():
            if error_label_symbols.winfo_exists():
                error_label_symbols.place_forget()
            if too_big_amount_of_symbols():
                if cannot_be_generated_label.winfo_exists():
                    cannot_be_generated_label.place_forget()
                if to_include_rus_check.get() or spec_symbols_check.get() or uppercase_letters_check.get():
                    result_entry['width'] = int(amount_of_symbols.get()) + 2
                else:
                    result_entry['width'] = int(amount_of_symbols.get()) + 1
                gen_alg()
                for i in result_list:
                    password += str(i)
            result_entry.insert(0, password)


# changing buttons values
global result_list
lowercase_letters['command'] = act_low
uppercase_letters['command'] = act_up
to_include_rus['command'] = lambda: [act_low(), act_up()]
to_include_eng['command'] = lambda: [act_low(), act_up()]
to_not_include_numbers['command'] = no_numbers
spec_symbols['command'] = act_symbols
gen_btn['command'] = gen_end
# running
window.mainloop()
