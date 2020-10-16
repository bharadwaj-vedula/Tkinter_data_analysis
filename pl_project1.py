#!/usr/bin/env python
# coding: utf-8

# In[41]:


import tkinter as tk
from tkinter import *
import sqlite3 as sql
import sys
import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt 
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


con =sql.connect('class_marks.db')
df_mt1=pd.read_excel("mt1.xlsx")
df_mt2=pd.read_excel("mt2.xlsx")


def datafetch1():
    
    x=listbox.get(listbox.curselection())
    index=listbox.curselection()
    print(x)
    plot1(index)

def datafetch2():
    ltxt=StringVar()
    x=listbox.get(listbox.curselection())
    index=listbox.curselection()
    plot2(index)
    
def plot1(index):
    root=tk.Tk()
    root.geometry("360x360")
    root.title('individual mark analysis mid term1')
    f=plt.Figure(figsize=(6,5))
    a=f.add_subplot(111)
    a.plot(df_mt1.iloc[index][3:10])
    a.plot([10,10,10,10,10,10,10])
    a.title.set_text("max marks vs your marks mid term1")
    a.set_ylim(2,14)
    canvas= FigureCanvasTkAgg(f, root)
    
    #canvas.show()
    canvas.get_tk_widget().pack(fill=tk.BOTH)
    root.mainloop()
    
def plot2(index):
    root=tk.Tk()
    root.geometry("360x360")
    root.title('individual mark analysis mid term2')
    f=plt.Figure(figsize=(6,5))
    a=f.add_subplot(111)
    a.plot(df_mt2.iloc[index][3:10])
    a.plot([10,10,10,10,10,10,10])
    a.title.set_text("max marks vs your marks mid term2 ")
    a.set_ylim(2,14)
    canvas= FigureCanvasTkAgg(f, root)
    #canvas.show()
    canvas.get_tk_widget().pack(fill=tk.BOTH)
    root.mainloop()

    



def disp_in_listbox():
    with con:
        cur=con.cursor()
        cur.execute("SELECT Roll_No FROM mt1")
        rows=cur.fetchall()
        for i in range(0,len(rows)):
            listbox.insert(END,rows[i])
    scbr1.config(command=listbox.yview)
    listbox.config(yscrollcommand=scbr1.set)
#gui
win=tk.Tk()
win.title('DATA VISUALISATION')
win.geometry('360x360')
#listbox
frame=LabelFrame(win)
frame.pack(padx=0,pady=10)
frame2=LabelFrame(win,borderwidth = 0, highlightthickness = 0)
frame2.pack()
listbox=Listbox(frame)
listbox.pack(side=LEFT,fill='both',expand=True )
scbr1=Scrollbar(frame)
scbr1.pack(side=RIGHT,fill='y')
#button
b1=Button(frame2,text="mid term1",command=datafetch1).pack(side=LEFT,padx=10,pady=10)
b2=Button(frame2,text="mid term2",command=datafetch2).pack(side=RIGHT,padx=10,pady=10)
                                                          
disp_in_listbox()  
win.mainloop()


# In[ ]:




