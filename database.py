from tkinter import *
from PIL import ImageTk, Image
import psycopg2


root = Tk()
root.title('Database')
root.geometry("350x500")
submit_btn0 = Button(root, text = "codes", command = '')
submit_btn1 = Button(root, text = "results", command = '')
submit_btn2 = Button(root, text = "code_characteristics", command = '')
submit_btn3 = Button(root, text = "code_parameters", command = '')
submit_btn4 = Button(root, text = "characteristics", command = '')
submit_btn5 = Button(root, text = "parameters", command = '')
submit_btn6 = Button(root, text = "elements", command = '')
submit_btn7 = Button(root, text = "processes", command = '')
submit_btn8 = Button(root, text = "devices", command = '')
submit_btn9 = Button(root, text = "versions", command = '')
submit_btn0.grid(row = 0, column = 0, columnspan=2, pady = 10, padx = 10, ipadx=100)
submit_btn1.grid(row = 1, column = 0, columnspan=2, pady = 10, padx = 10, ipadx=100)
submit_btn2.grid(row = 2, column = 0, columnspan=2, pady = 10, padx = 10, ipadx=100)
submit_btn3.grid(row = 3, column = 0, columnspan=2, pady = 10, padx = 10, ipadx=100)
submit_btn4.grid(row = 4, column = 0, columnspan=2, pady = 10, padx = 10, ipadx=100)
submit_btn5.grid(row = 5, column = 0, columnspan=2, pady = 10, padx = 10, ipadx=100)
submit_btn6.grid(row = 6, column = 0, columnspan=2, pady = 10, padx = 10, ipadx=100)
submit_btn7.grid(row = 7, column = 0, columnspan=2, pady = 10, padx = 10, ipadx=100)
submit_btn8.grid(row = 8, column = 0, columnspan=2, pady = 10, padx = 10, ipadx=100)
submit_btn9.grid(row = 9, column = 0, columnspan=2, pady = 10, padx = 10, ipadx=100)

root.mainloop()