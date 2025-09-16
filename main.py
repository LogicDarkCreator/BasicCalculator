# Import Libs
from configs.screen import *
from configs.btns import *
from tkinter import *


# Main Code
def btn_click(item):
    global expression
    try:
        input_field['state'] = state0
        expression += item
        input_field.insert(END, item)
        
        if item == "=":
            result = str(eval(expression[:-1]))
            input_field.insert(END, result)
            expression = ""
        
        input_field['state'] = state1
    except ZeroDivisionError:
        input_field.delete(0, END)
        input_field.insert(0, "Error (Cannot divide by Zero)")
    except SyntaxError:
        input_field.delete(0, END)
        input_field.insert(0, "Error")

def bt_clear():
    global expression
    expression = ""
    input_field['state'] = state0
    input_field.delete(0, END)
    input_field['state'] = state1


root = Tk()
root.geometry(size)
root.title(title)
root.resizable(r_width, r_height)

frame_input = Frame(root)
frame_input.grid(row=row, column=column, columnspan=columnspan, sticky=sticky)

input_field = Entry(frame_input, font=font, width=inputWidth, state=state1)
input_field.pack(fill=BOTH)

buttons = inputButtons

expression = ""

button = Button(root, text='C', command=lambda: bt_clear(), bg="#FF0000")
button.grid(row=1, column=3, sticky=sticky)

for row in range(4):
    for col in range(4):
        Button(root, width=2, height=3, text=buttons[row][col],
               command=lambda row=row, col=col: btn_click(buttons[row][col])).grid(row=row + 2, column=col, sticky="nsew", padx=1, pady=1)


root.mainloop()