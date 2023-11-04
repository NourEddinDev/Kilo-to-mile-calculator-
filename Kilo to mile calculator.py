import tkinter as tk
#from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    mile_input = entry_Int.get()
    km_output = mile_input * 1.61
    output_string.set(km_output)

#window
window = ttk.Window(themename = 'darkly')
window.title('Kilo to mile calculator')
window.geometry('300x150')


#title
title_label = ttk.Label(master = window, text = 'Miles to Kilometers', font = 'calibri 14 bold')
title_label.pack()
 
#input field
input_frame = ttk.Frame(master = window)
entry_Int = tk.IntVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_Int)
button = ttk.Button(master = input_frame, text = 'Convert', command = convert)
entry.pack(side = 'left', padx = 10)
button.pack(side = 'left')
input_frame.pack(pady = 10)

#output
output_string = tk.StringVar()
output_label = ttk.Label(
	master = window,
	text = 'output',
	font = 'calibri 24',
	textvariable = output_string)
output_label.pack(pady = 5)

#run
window.mainloop()