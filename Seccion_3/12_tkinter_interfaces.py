# -*- coding: utf-8 -*-
"""
Created on Wed May 11 21:44:32 2022

@author: carlsier
"""

#TKINTER INTERFACE
#SE DEBE ABRIR EN SPIDER, EN VS CODE NO ABRE

#GUI: interfaz de usuario tkinder pyqt5

from tkinter import *

app=Tk()
app.title("Fomulario")
app.geometry('300x300')

frame=Frame()
frame.grid(column=0, row=0, padx=(100,100), pady=(30,30))
frame.columnconfigure(0,weight=1)
frame.rowconfigure(0,weight=1)

etiqueta = Label(frame,text='Datos: ')
etiqueta.grid(column=6,rows=2)

entrada=Entry(frame,width='15')
entrada.grid(column=6, rows=5)

boton = Button(frame,text='guardar')
boton.grid(column=6, row=8)

app.mainloop()
