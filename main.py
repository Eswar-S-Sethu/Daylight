import tkinter as tk
import pygame as pyg
import pywhatkit as pywht
import time
import schedule as sch
import calendar as cl
import quote as qt
import python_weather as pyw

alarmsListWindow=tk.Tk()
alarmsListWindow.title("Alarms list")
alarmsListWindow.geometry("400x400")
allAlarmsLabel=tk.Label(alarmsListWindow,text="All alarms").pack()
newAlarmButton=tk.Button(alarmsListWindow,text="New Alarm",relief=tk.GROOVE).pack()

if __name__ == '__main__':
    alarmsListWindow.mainloop()


