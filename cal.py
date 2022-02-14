from tkinter import *
 
# declare global variable
text = ""
 
 
# to display the numbers in the box
def press(num):
    
    global text

    text = text + str(num)
 
    equation.set(text)
 
 
# Function to evaluate the final expression
def equalpress():
    # Try and except statement is used
    # for handling the errors like zero
    # division error etc.
 
    # Put that code inside the try block
    # which may generate the error
    try:
 
        global text
 
        # eval function evaluate the expression
        # and str function convert the result
        # into string
        total = str(eval(text))
 
        equation.set(total)
 
        # initialize the expression variable
        # by empty string
        text = ""
 
    # if error is generate then handle
    # by the except block
    except:
 
        equation.set(" error ")
        text = ""
 
 
# Function to clear the contents
# of text entry box
def clear():
    global text
    text = ""
    equation.set("")
 
 
# Driver code
if __name__ == "__main__":
    # create a GUI window
    gui = Tk()
    bg_colour = "#F0F0F0"
    # set the background colour of GUI window
    gui.configure(background=bg_colour)
 
    # set the title of GUI window
    gui.title("Simple Calculator")
 
    # set the configuration of GUI window
    gui.geometry("360x250")
 
    # StringVar() is the variable class
    # we create an instance of this class
    equation = StringVar()
 
    # create the text entry box for
    # showing the expression .
    text_field = Entry(gui, textvariable=equation)
 
    # grid method is used for placing
    # the widgets at respective positions
    # in table like structure .
    text_field.grid(columnspan=4, ipadx=70)
 
    button_height= 2
    button_width= 6
    button_colour= '#EAEAEA'
    text_colour= '#000000'
    button1 = Button(gui, text=' 1 ', fg=text_colour, bg=button_colour,
                    command=lambda: press(1), height=button_height, width=button_width)
    button1.grid(row=2, column=0)
 
    button2 = Button(gui, text=' 2 ', fg=text_colour, bg=button_colour,
                    command=lambda: press(2), height=button_height, width=button_width)
    button2.grid(row=2, column=1)
 
    button3 = Button(gui, text=' 3 ', fg=text_colour, bg=button_colour,
                    command=lambda: press(3), height=button_height, width=button_width)
    button3.grid(row=2, column=2)
 
    button4 = Button(gui, text=' 4 ', fg=text_colour, bg=button_colour,
                    command=lambda: press(4), height=button_height, width=button_width)
    button4.grid(row=3, column=0)
 
    button5 = Button(gui, text=' 5 ', fg=text_colour, bg=button_colour,
                    command=lambda: press(5), height=button_height, width=button_width)
    button5.grid(row=3, column=1)
 
    button6 = Button(gui, text=' 6 ', fg=text_colour, bg=button_colour,
                    command=lambda: press(6), height=button_height, width=button_width)
    button6.grid(row=3, column=2)
 
    button7 = Button(gui, text=' 7 ', fg=text_colour, bg=button_colour,
                    command=lambda: press(7), height=button_height, width=button_width)
    button7.grid(row=4, column=0)
 
    button8 = Button(gui, text=' 8 ', fg=text_colour, bg=button_colour,
                    command=lambda: press(8), height=button_height, width=button_width)
    button8.grid(row=4, column=1)
 
    button9 = Button(gui, text=' 9 ', fg=text_colour, bg=button_colour,
                    command=lambda: press(9), height=button_height, width=button_width)
    button9.grid(row=4, column=2)
 
    button0 = Button(gui, text=' 0 ', fg=text_colour, bg=button_colour,
                    command=lambda: press(0), height=button_height, width=button_width)
    button0.grid(row=5, column=1)
 
    plus = Button(gui, text=' + ', fg=text_colour, bg=button_colour,
                command=lambda: press("+"), height=button_height, width=button_width)
    plus.grid(row=2, column=3)
 
    minus = Button(gui, text=' - ', fg=text_colour, bg=button_colour,
                command=lambda: press("-"), height=button_height, width=button_width)
    minus.grid(row=3, column=3)
 
    multiply = Button(gui, text=' x ', fg=text_colour, bg=button_colour,
                    command=lambda: press("*"), height=button_height, width=button_width)
    multiply.grid(row=4, column=3)
 
    divide = Button(gui, text=' / ', fg=text_colour, bg=button_colour,
                    command=lambda: press("/"), height=button_height, width=button_width)
    divide.grid(row=5, column=3)
 
    equal = Button(gui, text=' = ', fg=text_colour, bg=button_colour,
                command=equalpress, height=button_height, width=button_width)
    equal.grid(row=5, column=2)
 
    clear = Button(gui, text='Clear', fg=text_colour, bg=button_colour,
                command=clear, height=button_height, width=button_width)
    clear.grid(row=6, column=0)
 
    Decimal= Button(gui, text='.', fg=text_colour, bg=button_colour,
                    command=lambda: press('.'), height=button_height, width=button_width)
    Decimal.grid(row=5, column=0)
    # start the GUI
    gui.mainloop()