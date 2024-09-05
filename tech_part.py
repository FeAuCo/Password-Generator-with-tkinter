import tkinter as tk
import random
import visual


# button's funcs
def act_low():
    visual.to_include_eng['state'] = tk.NORMAL
    visual.to_include_rus['state'] = tk.NORMAL
    if visual.lowercase_letters_check.get() is True:
        if visual.to_include_eng_check.get() is True:
            visual.password_el_dict.update({'eng_low_d': visual.eng_low})
        elif visual.to_include_eng_check.get() is False:
            try:
                visual.password_el_dict.pop('eng_low_d')
            except KeyError:
                pass
        if visual.to_include_rus_check.get() is True:
            visual.password_el_dict.update({'rus_low_d': visual.rus_low})
        elif visual.to_include_rus_check.get() is False:
            try:
                visual.password_el_dict.pop('rus_low_d')
            except KeyError:
                pass
    else:
        try:
            visual.password_el_dict.pop('rus_low_d')
        except KeyError:
            pass
        try:
            visual.password_el_dict.pop('eng_low_d')
        except KeyError:
            pass
        if visual.uppercase_letters_check.get() is False:
            visual.to_include_eng['state'] = tk.DISABLED
            visual.to_include_rus['state'] = tk.DISABLED


def act_up():
    visual.to_include_eng['state'] = tk.NORMAL
    visual.to_include_rus['state'] = tk.NORMAL
    if visual.uppercase_letters_check.get() is True:
        if visual.to_include_eng_check.get() is True:
            visual.password_el_dict.update({'eng_up_d': visual.eng_up})
        elif visual.to_include_eng_check.get() is False:
            try:
                visual.password_el_dict.pop('eng_up_d')
            except KeyError:
                pass
        if visual.to_include_rus_check.get() is True:
            visual.password_el_dict.update({'rus_up_d': visual.rus_up})
        elif visual.to_include_rus_check.get() is False:
            try:
                visual.password_el_dict.pop('rus_up_d')
            except KeyError:
                pass
    else:
        try:
            visual.password_el_dict.pop('rus_up_d')
        except KeyError:
            pass
        try:
            visual.password_el_dict.pop('eng_up_d')
        except KeyError:
            pass
        if visual.lowercase_letters_check.get() is False:
            visual.to_include_eng['state'] = tk.DISABLED
            visual.to_include_rus['state'] = tk.DISABLED


def no_numbers():
    if visual.to_not_include_numbers_check.get() is True:
        try:
            visual.password_el_dict.pop('numbers')
        except KeyError:
            pass
    else:
        visual.password_el_dict.update({'numbers': [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]})


def act_symbols():
    if visual.spec_symbols_check.get() is True:
        visual.password_el_dict.update({'symbols_d': visual.symbols})
    else:
        visual.password_el_dict.pop('symbols_d')


# checks
def check_amount_of_symbols():
    x_amount_of_symbols = visual.amount_of_symbols.get()
    try:
        x_amount_of_symbols = int(x_amount_of_symbols)
    except ValueError:
        visual.error_label_symbols.place(relx=.54, rely=.7, anchor="center")
        visual.amount_of_symbols.delete(0, tk.END)
        return False
    else:
        if x_amount_of_symbols <= 4:
            visual.error_label_symbols.place(relx=.54, rely=.7, anchor="center")
            visual.amount_of_symbols.delete(0, tk.END)
            return False
    return True


def gen_alg():
    global result_list
    result_list = []
    to_not_repeat_el_check_list = []
    list_with_listed_dict_values = [value_l for value_l in visual.password_el_dict.values()]
    for i in range(int(visual.amount_of_symbols.get())):
        list_to_choose_el_for_password = list_with_listed_dict_values[
            random.randint(0, len(list_with_listed_dict_values) - 1)]
        el_for_password = list_to_choose_el_for_password[random.randint(0, len(list_to_choose_el_for_password) - 1)]
        if visual.to_not_repeat_el_check.get() is False:
            result_list.append(el_for_password)
            to_not_repeat_el_check_list.append(el_for_password)
        elif visual.to_not_repeat_el_check.get() is True and el_for_password not in to_not_repeat_el_check_list:
            result_list.append(el_for_password)
            to_not_repeat_el_check_list.append(el_for_password)
        elif visual.to_not_repeat_el_check.get() is True and el_for_password in to_not_repeat_el_check_list:
            while el_for_password in to_not_repeat_el_check_list:
                list_to_choose_el_for_password = list_with_listed_dict_values[
                    random.randint(0, len(list_with_listed_dict_values) - 1)]
                el_for_password = list_to_choose_el_for_password[
                    random.randint(0, len(list_to_choose_el_for_password) - 1)]
            result_list.append(el_for_password)
            to_not_repeat_el_check_list.append(el_for_password)


# validating
def too_big_amount_of_symbols():
    if visual.to_not_repeat_el_check.get():
        if visual.to_not_include_numbers_check.get():
            x_amount_of_symbols = 0
        else:
            x_amount_of_symbols = 10
        if visual.spec_symbols_check.get():
            x_amount_of_symbols += 7
        if visual.uppercase_letters_check.get():
            if visual.to_include_eng_check.get():
                x_amount_of_symbols += 26
            if visual.to_include_rus_check.get():
                x_amount_of_symbols += 33
        if visual.lowercase_letters_check.get():
            if visual.to_include_eng_check.get():
                x_amount_of_symbols += 26
            if visual.to_include_rus_check.get():
                x_amount_of_symbols += 33
        if int(visual.amount_of_symbols.get()) > x_amount_of_symbols:
            visual.cannot_be_generated_label.place(relx=.54, rely=.7, anchor="center")
            return False
    return True


def cannot_be_generated():
    if visual.to_not_include_numbers_check.get() is True and visual.spec_symbols_check.get() is False and (
            (visual.uppercase_letters_check.get() is True or visual.lowercase_letters_check.get() is True) and (
            visual.to_include_eng_check.get() is False and visual.to_include_rus_check.get() is False) or (
                    visual.uppercase_letters_check.get() is False and visual.lowercase_letters_check.get() is False)):
        visual.cannot_be_generated_label.place(relx=.54, rely=.7, anchor="center")
        return False
    return True


def gen_end():
    visual.result_entry.delete(0, 'end')
    password = ''
    if cannot_be_generated():
        if visual.cannot_be_generated_label.winfo_exists():
            visual.cannot_be_generated_label.place_forget()
        if check_amount_of_symbols():
            if visual.error_label_symbols.winfo_exists():
                visual.error_label_symbols.place_forget()
            if too_big_amount_of_symbols():
                if visual.cannot_be_generated_label.winfo_exists():
                    visual.cannot_be_generated_label.place_forget()
                if (visual.to_include_rus_check.get() or visual.spec_symbols_check.get() or
                        visual.uppercase_letters_check.get()):
                    visual.result_entry['width'] = int(visual.amount_of_symbols.get()) + 2
                else:
                    visual.result_entry['width'] = int(visual.amount_of_symbols.get()) + 1
                gen_alg()
                for i in result_list:
                    password += str(i)
            visual.result_entry.insert(0, password)


# changing buttons values
global result_list
visual.lowercase_letters['command'] = act_low
visual.uppercase_letters['command'] = act_up
visual.to_include_rus['command'] = lambda: [act_low(), act_up()]
visual.to_include_eng['command'] = lambda: [act_low(), act_up()]
visual.to_not_include_numbers['command'] = no_numbers
visual.spec_symbols['command'] = act_symbols
visual.gen_btn['command'] = gen_end
# running
visual.window.mainloop()
