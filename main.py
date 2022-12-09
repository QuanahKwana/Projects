import tkinter as tk

numField = ""

#adds input on screen to be solved
def input(nums):
    global numField
    numField += str(nums)
    answer.delete(1.0, "end")
    answer.insert(1.0, numField)

#solve the input
def solve():
    global numField
    try:
        numField = str(eval(numField))
        answer.delete(1.0, "end")
        answer.insert(1.0, numField)
    except:
        clear()
        answer.insert(1.0, "Error")


#clear the input
def clear():
    global numField
    numField = ""
    answer.delete(1.0, "end")


window = tk.Tk()
window.geometry("300x350")

answer = tk.Text(window, width=11, height=2, font=("Impact", 36))
answer.grid(columnspan=5)

but1 = tk.Button(window, text="1", font=("Impact", 12), command=lambda: input(1), width=6)
but1.grid(row=4, column=1)

but2 = tk.Button(window, text="2", font=("Impact", 12), command=lambda: input(2), width=6)
but2.grid(row=4, column=2)

but3 = tk.Button(window, text="3", font=("Impact", 12), command=lambda: input(3), width=6)
but3.grid(row=4, column=3)

but4 = tk.Button(window, text="4", font=("Impact", 12), command=lambda: input(4), width=6)
but4.grid(row=3, column=1)

but5 = tk.Button(window, text="5", font=("Impact", 12), command=lambda: input(5), width=6)
but5.grid(row=3, column=2)

but6 = tk.Button(window, text="6", font=("Impact", 12), command=lambda: input(6), width=6)
but6.grid(row=3, column=3)

but7 = tk.Button(window, text="7", font=("Impact", 12), command=lambda: input(7), width=6)
but7.grid(row=2, column=1)

but8 = tk.Button(window, text="8", font=("Impact", 12), command=lambda: input(8), width=6)
but8.grid(row=2, column=2)

but9 = tk.Button(window, text="9", font=("Impact", 12), command=lambda: input(9), width=6)
but9.grid(row=2, column=3)

but0 = tk.Button(window, text="0", font=("Impact", 12), command=lambda: input(0), width=6)
but0.grid(row=5, column=1)

plus = tk.Button(window, text="+", font=("Impact", 12), command=lambda: input("+"), width=6)
plus.grid(row=1, column=4)

openpar = tk.Button(window, text="(", font=("Impact", 12), command=lambda: input("("), width=6)
openpar.grid(row=1, column=2)

closepar = tk.Button(window, text=")", font=("Impact", 12), command=lambda: input(")"), width=6)
closepar.grid(row=1, column=3)

minus = tk.Button(window, text="-", font=("Impact", 12), command=lambda: input("-"), width=6)
minus.grid(row=2, column=4)

mult = tk.Button(window, text="x", font=("Impact", 12), command=lambda: input("*"), width=6)
mult.grid(row=3, column=4)

div = tk.Button(window, text="÷", font=("Impact", 12), command=lambda: input("/"), width=6)
div.grid(row=4, column=4)

sqrt = tk.Button(window, text="√", font=("Impact", 12), command=lambda: input("sqrt("), width=6)
sqrt.grid(row=1, column=1)

c = tk.Button(window, text="Clear!", font=("Impact", 12), command=clear, width=6)
c.grid(row=5, column=2)

enter = tk.Button(window, text="Enter!", font=("Impact", 12), command=solve, width=15)
enter.grid(row=5, column=3, columnspan=2)



window.mainloop()
