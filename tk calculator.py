#import tkinter
import tkinter as tk
root = tk.Tk()

# add title
root.title("Calculator")

# window properties
root.geometry("300x200")
root.resizable(True, True)


# sums functions

def add(data):
    data = data.split('+')
    no1 = data[0]
    no2 = data[1]
    return int(no1)+int(no2)

def sub(data):
    data = data.split('-')
    no1 = data[0]
    no2 = data[1]
    return int(no1)-int(no2)

def multiply(data):
    data = data.split('x')
    no1 = data[0]
    no2 = data[1]
    return int(no1)*int(no2)

def divide(data):
    data = data.split('/')
    no1 = data[0]
    no2 = data[1]
    return int(no1)//int(no2)



operators = ['+','-','x','/']


# button pressed functions
def seven_pressed():
    output_entry.insert(200,"7")
def eight_pressed():
    output_entry.insert(200,'8')
def nine_pressed():
    output_entry.insert(200,'9')
def clear_pressed():
    output_entry.delete(0,200)
def four_pressed():
    output_entry.insert(200,'4')
def five_pressed():
    output_entry.insert(200,'5')
def six_pressed():
    output_entry.insert(200,'6')
def plus_pressed():
    output_entry.insert(200,'+')
def one_pressed():
    output_entry.insert(200,"1")
def two_pressed():
    output_entry.insert(200,"2")
def three_pressed():
    output_entry.insert(200,"3")
def minus_pressed():
    output_entry.insert(200,"-")
def zero_pressed():
    output_entry.insert(200,"0")
def divide_pressed():
    output_entry.insert(200,"/")
def multiply_pressed():
    output_entry.insert(200,"x")
def equal_pressed():
    answer = output_entry.get()
    output_entry.delete(0,200)
    for i in answer:
        if i == "+":
            ans = add(answer)
            output_entry.insert(200,str(ans))
        if i == "-":
            ans = sub(answer)
            output_entry.insert(200,str(ans))
        if i == "x":
            ans = multiply(answer)
            output_entry.insert(200,str(ans))
        if i == "/":
            ans = divide(answer)
            output_entry.insert(200,str(ans))
        







#configure grid
for rowcol in range(6):
    root.rowconfigure(rowcol, weight = 1)
    root.columnconfigure(rowcol, weight = 1)
root.rowconfigure(5,weight = 2)

#create widgets
title_label = tk.Label (root, text = "Calculator", font = ("Arial",14))
output_entry = tk.Entry(root)
seven_button = tk.Button (root, text = "    7    ", command = seven_pressed )
eight_button = tk.Button (root, text = "    8    ", command = eight_pressed)
nine_button = tk.Button (root, text = "    9    ", command = nine_pressed)
clear_button = tk.Button (root, text = "   AC   ", command = clear_pressed)
four_button = tk.Button (root, text = "    4    ", command = four_pressed)
five_button = tk.Button (root, text = "    5    ", command = five_pressed)
six_button = tk.Button (root, text = "    6    ", command = six_pressed)
plus_button = tk.Button (root, text = "    +    ", command = plus_pressed)
one_button = tk.Button (root, text = "    1    ", command = one_pressed)
two_button = tk.Button (root, text = "    2    ", command = two_pressed)
three_button = tk.Button (root, text = "    3    ", command = three_pressed)
minus_button = tk.Button (root, text = "    -    ", command = minus_pressed)
zero_button = tk.Button (root, text = "    0    ", command = zero_pressed)
divide_button = tk.Button (root, text = "    /    ", command = divide_pressed)
multiply_button = tk.Button (root, text = "    x    ", command = multiply_pressed)
equal_button = tk.Button (root, text = "    =    ", command = equal_pressed)

title_label.grid (row=0, column=0, columnspan=5)
output_entry.grid (row=1, column=0, columnspan=5)
seven_button.grid (row= 2, column=0)
eight_button.grid (row= 2, column=1)
nine_button.grid (row= 2, column=2)
clear_button.grid (row= 2, column=3)
four_button.grid (row= 3, column=0)
five_button.grid (row= 3, column=1)
six_button.grid (row= 3, column=2)
plus_button.grid (row= 3, column=3)
one_button.grid (row= 4, column=0)
two_button.grid (row= 4, column=1)
three_button.grid (row= 4, column=2)
minus_button.grid (row= 4, column=3)
zero_button.grid (row= 5, column=0)
divide_button.grid (row= 5, column=1)
multiply_button.grid (row= 5, column=2)
equal_button.grid (row= 5, column=3)
                          
#main loop
root.mainloop()











