import pyautogui as p
import time
import datetime as dt
import selenium
from selenium import webdriver
from tkinter import *
from tkcalendar import Calendar
from PIL import ImageTk, Image 
import os
import urllib

options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome(options=options)
root=Tk()
root.title("Weather")
root.geometry("925x600")
root.maxsize(925,600)
root.minsize(925,600)
def getWeather(date,city):
    date=date.split("/")
    date=date[::-1]
    date='/'.join(date)
    tokyoLink="https://www.wunderground.com/history/daily/jp/tokyo/RJTT/date/20"
    parisLink="https://www.wunderground.com/history/daily/fr/paray-vieille-poste/LFPO/date/20"
    ankaraLink="https://www.wunderground.com/history/daily/tr/çubuk/LTAC/date/20"
    romaLink="https://www.wunderground.com/history/daily/it/ciampino/LIRA/date/20"
    if city=="Tokyo":
        url=tokyoLink+date
        img = ImageTk.PhotoImage(Image.open("tokyo.jpeg"))
        panel =Label(root, image = img)
        panel.place(x=325,y=0)
    if city=="Paris":
        url=parisLink+date
        img = ImageTk.PhotoImage(Image.open("paris.jpeg"))
        panel =Label(root, image = img)
        panel.place(x=325,y=0)
    if city=="Ankara":    
        url=ankaraLink+date
        img = ImageTk.PhotoImage(Image.open("ankara.jpeg"))
        panel =Label(root, image = img)
        panel.place(x=325,y=0)
    if city=="Roma":
        url=romaLink+date
        img = ImageTk.PhotoImage(Image.open("roma.jpeg"))
        panel =Label(root, image = img)
        panel.place(x=325,y=0)
    driver.get(url)
    time.sleep(2)
    max_Temperature = driver.find_element("xpath","/html/body/app-root/app-history/one-column-layout/wu-header/sidenav/mat-sidenav-container/mat-sidenav-content/div/section/div[2]/div[1]/div[3]/div[1]/div/lib-city-history-summary/div/div[2]/table/tbody[1]/tr[1]/td[1]")
    min_Temperature = driver.find_element("xpath","/html/body/app-root/app-history/one-column-layout/wu-header/sidenav/mat-sidenav-container/mat-sidenav-content/div/section/div[2]/div[1]/div[3]/div[1]/div/lib-city-history-summary/div/div[2]/table/tbody[1]/tr[2]/td[1]")
    avr_Temperature = driver.find_element("xpath","/html/body/app-root/app-history/one-column-layout/wu-header/sidenav/mat-sidenav-container/mat-sidenav-content/div/section/div[2]/div[1]/div[3]/div[1]/div/lib-city-history-summary/div/div[2]/table/tbody[1]/tr[3]/td[1]")
    max=max_Temperature.text
    min=min_Temperature.text
    davr=avr_Temperature.text
    max=round(((float(max)-32)/1.8),2)
    min=round(((float(min)-32)/1.8),2)
    davr=round(((float(davr)-32)/1.8),2)    
    print(url)
    label=Label(root,text="On 20{} in {}".format(date,city),anchor = "w",font=("Arial",11))
    label.place(x=15,y=480)
    label1=Label(root,text="Max temperature: {}°  ".format(max),anchor = "w",font=("Arial",11))
    label1.place(x=15,y=510)
    label2=Label(root,text="Min temperature: {}°   ".format(min),anchor = "w",font=("Arial",11))
    label2.place(x=15,y=540)
    label3=Label(root,text="Average temperature: {}°    ".format(davr),anchor = "w",font=("Arial",11))
    label3.place(x=15,y=570)
    root.mainloop()
#creating listbox
Lb1 = Listbox(root,font=("Arial",14,"bold"))
Lb1.insert(1, "Tokyo")
Lb1.insert(2, "Paris")
Lb1.insert(3, "Ankara")
Lb1.insert(4, "Roma")
Lb1.place(x=25,y=0)
#put jpeg file to panel
img = ImageTk.PhotoImage(Image.open("stock.jpeg"))
panel =Label(root, image = img)
panel.place(x=325,y=0)
def getData():
    try:
        urllib.request.urlopen("https://www.google.com/")
        try:
            date=cal.get_date()
            for i in Lb1.curselection():
                city=Lb1.get(i)
        
            getWeather(date,city)    
        except UnboundLocalError:
            check=p.confirm("Please pick city",buttons=["Okay"])
    except :
        check=p.confirm("Please check your internet connection",buttons=["Okay"])       
#date tasarım
today = dt.datetime.today()
mindate=dt.datetime(2000,1,1)
cal = Calendar(root, selectmode = 'day',maxdate=today,mindate=mindate)
cal.place(x=15,y=225)
#button
btn = Button(root, text='Get weather',font=("Arial",12), command=getData)
btn.place(x=15,y=440)
root.mainloop()
driver.close()