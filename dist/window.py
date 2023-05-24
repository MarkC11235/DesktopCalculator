import tkinter as tk

# Create a window
window = tk.Tk()

# Set the window title
window.title("Calculator")

# Set the window icon
window.iconbitmap("calculator_Icon.ico")

# Set the window size
window.geometry("320x360")

font = ("Arial", 20, "bold")
borderwidth = 0

# Create a label
label = tk.Label(window, text="", font = font, borderwidth=borderwidth)

def button_click(text):
    if(text == "Clr"):
        label["text"] = ""
    elif(text == "="):
        label["text"] = label["text"].replace("^", "**")
        label["text"] = eval(label["text"]).__str__()
    else:
        label["text"] += text

# Create a button
button_0 = tk.Button(window, text="0",command=lambda: button_click('0'), font = font, borderwidth=borderwidth)
button_1 = tk.Button(window, text="1",command=lambda: button_click('1'), font = font, borderwidth=borderwidth)
button_2 = tk.Button(window, text="2",command=lambda: button_click('2'), font = font, borderwidth=borderwidth)
button_3 = tk.Button(window, text="3",command=lambda: button_click('3'), font = font, borderwidth=borderwidth)
button_4 = tk.Button(window, text="4",command=lambda: button_click('4'), font = font, borderwidth=borderwidth)
button_5 = tk.Button(window, text="5",command=lambda: button_click('5'), font = font, borderwidth=borderwidth)
button_6 = tk.Button(window, text="6",command=lambda: button_click('6'), font = font, borderwidth=borderwidth)
button_7 = tk.Button(window, text="7",command=lambda: button_click('7'), font = font, borderwidth=borderwidth)
button_8 = tk.Button(window, text="8",command=lambda: button_click('8'), font = font, borderwidth=borderwidth)
button_9 = tk.Button(window, text="9",command=lambda: button_click('9'), font = font, borderwidth=borderwidth)
button_plus = tk.Button(window, text="+",command=lambda: button_click('+'), font = font, borderwidth=borderwidth)
button_minus = tk.Button(window, text="-",command=lambda: button_click('-'), font = font, borderwidth=borderwidth)
button_multiply = tk.Button(window, text="*",command=lambda: button_click('*'), font = font, borderwidth=borderwidth)
button_divide = tk.Button(window, text="/",command=lambda: button_click('/'), font = font, borderwidth=borderwidth)
button_equal = tk.Button(window, text="=",command=lambda: button_click('='), font = font, borderwidth=borderwidth)
button_clear = tk.Button(window, text="Clr",command=lambda: button_click('Clr'), font = font, borderwidth=borderwidth)
button_dot = tk.Button(window, text=".",command=lambda: button_click('.'), font = font, borderwidth=borderwidth)
button_left_bracket = tk.Button(window, text="(",command=lambda: button_click('('), font = font, borderwidth=borderwidth)
button_right_bracket = tk.Button(window, text=")",command=lambda: button_click(')'), font = font, borderwidth=borderwidth)
button_power = tk.Button(window, text="^",command=lambda: button_click('^'), font = font, borderwidth=borderwidth)

# Add the label to the window
label.grid(row=0, column=0, columnspan=4)

# Add the button to the window
button_0.grid(row=4, column=1)
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_plus.grid(row=1, column=3)
button_minus.grid(row=2, column=3)
button_multiply.grid(row=3, column=3)
button_divide.grid(row=4, column=3)
button_equal.grid(row=4, column=2)
button_clear.grid(row=4, column=0)
button_dot.grid(row=5, column=0)
button_left_bracket.grid(row=5, column=1)
button_right_bracket.grid(row=5, column=2)
button_power.grid(row=5, column=3)

# Configure the grid to span the whole window
for i in range(4):
    window.columnconfigure(i, weight=1)
for i in range(6):
    window.rowconfigure(i, weight=1)

# Display the window
window.mainloop()