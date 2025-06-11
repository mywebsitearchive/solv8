import tkinter as tk
from tkinter import font
import random
import math

win = tk.Tk()
win.geometry("800x500")

f = tk.Frame(win, padx = 100, pady=25, bg = 'cyan2')
f.grid_columnconfigure(0, minsize=80)
f.grid_columnconfigure(1, minsize=80)
f.grid_columnconfigure(2, minsize=80)
f.grid_columnconfigure(3, minsize=80)
f.grid_columnconfigure(4, minsize=80)
f.grid_columnconfigure(5, minsize=80)
f.grid_rowconfigure(3, minsize=100)
f.pack()

custom_font = font.Font(size=25)

debug_element = tk.Label(f, text = "debug", relief = "groove")
debug2_element = tk.Label(f, text = "debug2", relief = "groove")
i = 0
equation_line = ["", "", "", "", ""]
equation_line_text = ""
beginning = True
attempt = 0
wanted_number = 0
used_numbers = []


def update_line(x): # x = 1-5 or symbol
    global i
    global equation_line
    global equation_line_text
    global beginning
    global result
    global wanted_number
    global attempt
    global used_numbers
    if i % 2 == 0: # i = 0,2,4 -> number
        if str(x).isnumeric():
            equation_line[i] = numbers[int(x)]
            i += 1
            debug_element.config(text = equation_line)
            debug_element.config(text = 'x' + str(x))
            lock_button(x)
            update_background(i, x)
            used_numbers.insert(0, x)
    elif i < 5 : # i = 1, 3 -> symbol
        if not str(x).isnumeric():
            equation_line[i] = x
            i += 1
            debug_element.config(text = equation_line)
            update_background(i, x)
            used_numbers.insert(0, x)
    elif x == "5": # last number pressed
        debug_element.config(text = 'x' + str(x))
        lock_button(x)
        i = 0
        for no in range(5):
            equation_line_text += str(equation_line[no])
        result = eval(equation_line_text)
        your_number_element.config(text = result)
        attempt += 1
        if result == wanted_number:
            play_again_btn.grid(row=3, column=1, columnspan=5)
            wanted_number_element.config(text="You win! Attempts: " + str(attempt))
            sym1_element.config(state="disabled")
            sym2_element.config(state="disabled")
            sym3_element.config(state="disabled")
            sym4_element.config(state="disabled")
            sym5_element.config(state="disabled")
            num1_element.config(state="disabled")
            num2_element.config(state="disabled")
            num3_element.config(state="disabled")
            num4_element.config(state="disabled")
            num5_element.config(state="disabled")

        else:
            equation_line = [result, "", "", "", ""]
            if result > 999:
                result = 999
            debug_element.config(text = "result: " + str(result))
            equation_line_text = ""
            update_background(i, x)
            empty_inputs()
            beginning = False
            draw_numbers()
            debug2_element.config(text="attempts: " + str(attempt))

def lock_button(x):
    if str(x).isnumeric():
        match int(x)+1:
            case 1:
                num1_element.config(state="disabled")
            case 2:
                num2_element.config(state="disabled")
            case 3:
                num3_element.config(state="disabled")
            case 4:
                num4_element.config(state="disabled")
            case 5:
                num5_element.config(state="disabled")


def update_background(i, x):
    i1_element.config(bg='white')
    i2_element.config(bg='white')
    i3_element.config(bg='white')
    i4_element.config(bg='white')
    i5_element.config(bg='white')
    match i:
        case 1:
            i2_element.config(bg='green1')
            i1_element.config(text=numbers[int(x)])
        case 2:
            i3_element.config(bg='green1')
            i2_element.config(text=x)
        case 3:
            i4_element.config(bg='green1')
            i3_element.config(text=numbers[int(x)])
        case 4:
            i5_element.config(bg='green1')
            i4_element.config(text=x)
        case 5:
            i5_element.config(text=numbers[int(x)])

def empty_inputs():
    i1_element.config(bg='green1')
    i1_element.config(text="_")
    i2_element.config(text="_")
    i3_element.config(text="_")
    i4_element.config(text="_")
    i5_element.config(text="_")

def draw_numbers():
    global numbers
    global symbols
    global equation_line
    global i
    global wanted_number
    if beginning:
        wanted_number = random.randrange(75,150)
        wanted_number_element.config(text = "Goal: " + str(wanted_number))
    else:
        equation_line[0] = math.floor(result)
        debug_element.config(text=equation_line)
        i1_element.config(text=math.floor(result))
        i = 1
        i2_element.config(bg='green1')
        i1_element.config(bg='white')
        num1_element.config(state="active")
        num2_element.config(state="active")
        num3_element.config(state="active")
        num4_element.config(state="active")
        num5_element.config(state="active")

    a = random.randrange(2,5)
    b = random.randrange(6,9)
    c = random.randrange(10,15)
    d = random.randrange(16,25)
    e = random.randrange(25,40)
    symbols = ["+","x","-","/"]
    numbers = [a, b, c, d, e]
    random.shuffle(numbers)
    num1_element.config(text = numbers[0])
    num2_element.config(text = numbers[1])
    num3_element.config(text = numbers[2])
    num4_element.config(text = numbers[3])
    num5_element.config(text = numbers[4])
    sym1_element.config(text = symbols[0])
    sym2_element.config(text = symbols[1])
    sym3_element.config(text = symbols[2])
    sym4_element.config(text = symbols[3])

def clear_backgrounds():
    i1_element.config(bg='white')
    i2_element.config(bg='white')
    i3_element.config(bg='white')
    i4_element.config(bg='white')
    i5_element.config(bg='white')

def backspace():
    global equation_line
    global i
    global used_numbers
    if (i > 0 and beginning) or i > 1:
        clear_backgrounds()
        match i:
            case 1:
                i1_element.config(bg='green1', text="_")
            case 2:
                i2_element.config(bg='green1', text="_")
            case 3:
                i3_element.config(bg='green1', text="_")
            case 4:
                i4_element.config(bg='green1', text="_")
            case 5:
                i5_element.config(bg='green1', text="_")
        equation_line[i-1]=""
        i-=1
        
        if str(used_numbers[0]).isnumeric():
            match int(used_numbers[0])+1:
                case 1:
                    num1_element.config(state="active")
                case 2:
                    num2_element.config(state="active")
                case 3:
                    num3_element.config(state="active")
                case 4:
                    num4_element.config(state="active")
                case 5:
                    num5_element.config(state="active")
            debug2_element.config(text=used_numbers)
        else:
            debug2_element.config(text="symbol: "+used_numbers[0])
        used_numbers.pop(0)


def play_again():
    global beginning
    global attempt
    global result
    global i
    global equation_line
    global equation_line_text
    i = 0
    equation_line_text = ""
    equation_line = ["", "", "", "", ""]
    result = 0
    your_number_element.config(text=str(result))
    debug2_element.config(text=result)
    empty_inputs()
    clear_backgrounds()
    attempt = 0
    sym1_element.config(state="active")
    sym2_element.config(state="active")
    sym3_element.config(state="active")
    sym4_element.config(state="active")
    sym5_element.config(state="active")
    num1_element.config(state="active")
    num2_element.config(state="active")
    num3_element.config(state="active")
    num4_element.config(state="active")
    num5_element.config(state="active")
    play_again_btn.grid_forget()
    beginning = True
    draw_numbers()

play_again_btn = tk.Button(f,text = "Play Again", command=play_again, font=custom_font)
wanted_number_element = tk.Label(f,text = "wanted number", relief = "groove", font=custom_font)
your_number_element = tk.Label(f,text = "your number", relief = "groove", font=custom_font)
i1_element = tk.Label(f,text = "_", relief = "groove", width=3, bg='green1', font=custom_font)
i2_element = tk.Label(f,text = "_", relief = "groove", width=3, font=custom_font)
i3_element = tk.Label(f,text = "_", relief = "groove", width=3, font=custom_font)
i4_element = tk.Label(f,text = "_", relief = "groove", width=3, font=custom_font)
i5_element = tk.Label(f,text = "_", relief = "groove", width=3, font=custom_font)
empty_row_element = tk.Label(f, bg='cyan2')
sym1_element = tk.Button(f, text = " ", command = lambda: update_line("+"), width=3, font=custom_font)
sym2_element = tk.Button(f, text = " ", command = lambda: update_line("*"), width=3, font=custom_font)
sym3_element = tk.Button(f, text = " ", command = lambda: update_line("-"), width=3, font=custom_font)
sym4_element = tk.Button(f, text = " ", command = lambda: update_line("/"), width=3, font=custom_font)
sym5_element = tk.Button(f, text = "⌫", command = backspace, width=3, font=custom_font)
num1_element = tk.Button(f, text = " ", command = lambda: update_line("0"), width=3, font=custom_font)
num2_element = tk.Button(f, text = " ", command = lambda: update_line("1"), width=3, font=custom_font)
num3_element = tk.Button(f, text = " ", command = lambda: update_line("2"), width=3, font=custom_font)
num4_element = tk.Button(f, text = " ", command = lambda: update_line("3"), width=3, font=custom_font)
num5_element = tk.Button(f, text = " ", command = lambda: update_line("4"), width=3, font=custom_font)
submitbutton = tk.Button(f, text = "Submit", command= lambda: update_line("5") , font=custom_font)
topbar = tk.Label(f,text = "____", relief = "groove")

wanted_number_element.grid(row = 1, column = 1, columnspan = 5)
your_number_element.grid(row = 0, column = 1, columnspan = 5)
i1_element.grid(row = 2, column = 1)
i2_element.grid(row = 2, column = 2)
i3_element.grid(row = 2, column = 3)
i4_element.grid(row = 2, column = 4)
i5_element.grid(row = 2, column = 5)
empty_row_element.grid(row = 3)
play_again_btn.grid_forget()
sym1_element.grid(row = 4, column = 1)
sym2_element.grid(row = 4, column = 2)
sym3_element.grid(row = 4, column = 3)
sym4_element.grid(row = 4, column = 4)
sym5_element.grid(row = 4, column = 5)
num1_element.grid(row = 5, column = 1)
num2_element.grid(row = 5, column = 2)
num3_element.grid(row = 5, column = 3)
num4_element.grid(row = 5, column = 4)
num5_element.grid(row = 5, column = 5)
submitbutton.grid(row = 6, column=1, columnspan=5)
debug_element.grid(row = 7, column=1, columnspan=5)
debug2_element.grid(row = 8, column=1, columnspan=5)


draw_numbers()

win.mainloop()
