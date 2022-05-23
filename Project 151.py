from tkinter import *
import random
root = Tk()
root.geometry("400x400")
root.title("Project 151")
month = ("January", "Febuary", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
profits = (1837, 19827, 1937, 19837, 19237, 1908, 1938, 19387, 12183, 19873, 19279, 1999)
month_value = Label(root)
profit_value = Label(root)
maximum_profit = Label(root)
minimum_profit = Label(root)

def profit() :
    max_profit = max(profit)
    max_profit_index = profits.index(max_profit)
    maximum_profit["text"] = str(max_profit_index)
    max_profit_month = month_value[max_profit_index]
    maximum_profit["text"] = "The maximum profit is " + str(max_profit) + ". This was in the month of " + str(max_profit_month) + "." + "\n"
    min_profit = min(profits)
    min_profit_index = profits.index(min_profit)
    minimum_profit["text"] = str(min_profit_index)
    min_profit_month = month_value[min_profit_index]
    minimum_profit["text"] = "The minimum profit is " + str(min_profit) + ". The was in the month of " + str(min_profit_month) + "." + "\n"
    
btn = Button(root, text = "Show Profits", command = profit)
btn.place(relx = 0.5, rely = 0.5, anchor = CENTER)
maximum_profit.place(relx = 0.5, rely = 0.3, anchor = CENTER)
minimum_profit.place(relx = 0.5, rely = 0.4, anchor = CENTER)
month_value["text"] = "" + str(month)
profit_value["text"] = "" + str(profits)
month_value.place(relx = 0.5, rely = 0.6, anchor = CENTER)
profit_value.place(relx = 0.5, rely = 0.7, anchor = CENTER)
root.mainloop()