#from tkinter import *
import tkinter as tk
from tkinter.ttk import *
from tkinter.filedialog import askopenfile 
import time
import os.path
import pandas as pd



ws =tk.Tk()
ws.title('PythonGuides')
ws.geometry('400x200')


import subprocess

def callback1():
    cmd = 'python3 finalmarts.py'

    # it will execute script which runs only `function1`
    output = subprocess.check_output(cmd, shell=True)
    lbl['text'] = output.strip()
class StdoutRedirector(object):

    def __init__(self):
        # clear before get all values
        self.result = ''

    def write(self, text):
        # have to use += because one `print()` executes `sys.stdout` many times
        self.result += text

import sys

class StdoutRedirectorLabel(object):

    def __init__(self, widget):
        self.widget = widget
        # clear at start because it will use +=
        self.widget['text'] = ''

    def write(self, text):
        # have to use += because one `print()` executes `sys.stdout` many times
        self.widget['text'] += text

def open_file():
    file_path = askopenfile(mode='r', filetypes=[('Excel', '*xlsx')])
    global filename
    filename=file_path.name    
    print(filename)
    if file_path is not None:
        pass


def uploadFiles():
    print(filename)
    if filename is not None:
        print("THERE WAS A FILEPATH")
        function1()
        excel_data_df = pd.read_excel(filename)
        df = pd.DataFrame(excel_data_df, columns=['Gender'])
        counts = df.value_counts()
        print(excel_data_df)
        print(counts)
        Label(ws, text='File Uploaded Successfully!', foreground='green').grid(row=4, columnspan=3, pady=10)
        print("DONE")
    else:
        print("NO VALID FILEPATH")

xlsxL = Label(
    ws, 
    text='Upload XLSX spreadsheet file '
    )
xlsxL.grid(row=0, column=0, padx=10)

adharbtn = Button(
    ws, 
    text ='Choose File', 
    command = lambda:open_file()
    ) 
adharbtn.grid(row=0, column=1)

upld = Button(
    ws, 
    text='Upload Files', 
    command= lambda:uploadFiles()
    )
upld.grid(row=3, columnspan=3, pady=10)
lbl = Label(
    ws, 
    text=''
    )
lbl.grid(row=0, column=0, padx=10)

btn1 = tk.Button(ws, text="subprocess", command=callback1)
btn1.grid(row=3, columnspan=4,pady=10)

ws.mainloop()
