import time
import threading
import pandas as pd
import tkinter as tk
from getTime import getTime
import export_to_excel as excel
import dataApi as api

excel.data.updateExcel()

#เวลาบนโปรแกรม
def runTime():
    while True:
        #date
        label_date = add.label(text = 'Current Date :' , row = 0 , column = 0 , padx = (5,0) , pady = (5,0))
        current_date = add.label(text = getTime.date() , row = 0 , column = 1 , padx = (0,0) , pady = (5,0))

        #time
        label_time = add.label(text = 'Current Time :' , row = 1 , column = 0 , padx = (5,0) , pady = (0,0))
        current_time = add.label(text = getTime.time() , row = 1 , column = 1 , padx = (0,0) , pady = (0,0))

        # current_time['text'] = getTime.time()
        # current_date['text'] = getTime.date()
        time.sleep(0.2)

class add :
    def label (text , row , column , padx , pady , rowspan = 1 , columnspan = 1 , font_size = 10) :
        data = tk.Label(master = frame , text = text)
        data.grid(row = row , rowspan = rowspan , column = column , columnspan = columnspan , padx = padx , pady = pady)
        data.config(font = ('Tahoma' , font_size))
        return data

    def entry (width , row , column , padx , pady , rowspan = 1 , columnspan = 1 , justify = 'center') :
        data = tk.Entry(master = frame , width = width , justify = justify)
        data.grid(row = row , rowspan = rowspan , column = column , columnspan = columnspan , padx = padx , pady = pady)
        return data

    def button (text , row , column , padx , pady , rowspan = 1 , columnspan = 1 , command = '' , font_size = 10) :
        data = tk.Button(master = frame , text = text , command = command)
        data.grid(row = row , rowspan = rowspan , column = column , columnspan = columnspan , padx = padx , pady = pady)
        data.config(font = ('Tahoma' , font_size))
        return data

    def optionMenu(text , options , row , column , padx , pady , rowspan = 1 , columnspan = 1 , command = '' , font_size = 10) :
        variable = tk.StringVar(frame)
        variable.set(text)
        data = tk.OptionMenu(frame , variable , *options , command = command)
        data.grid(row = row , rowspan = rowspan , column = column , columnspan = columnspan , padx = padx , pady = pady)
        data.config(font = ('Tahoma' , font_size))
        return data

def addStockList() :
    clearScreen()
    def addList() :
        api.data.post(name_entry.get() , description_entry.get() , amount_entry.get() , price_entry.get())
       
    addList_label = add.label(text = 'เพิ่มรายการสินค้าในระบบ' , row = 1 , column = 2 , padx = (0,0) , pady = (0,0))

    name_label = add.label(text = 'ชื่อสินค้า' , row = 2 , column = 0 , columnspan = 2 , padx = (0,0) , pady = (10,0))
    name_entry = add.entry(width = 50 , row = 2 , column = 2 , padx = (0,0) , pady = (10,0))

    description_label = add.label(text = 'คำอธิบายสินค้า' , row = 3 , column = 0 , columnspan = 2 , padx = (0,0) , pady =(5,0))
    description_entry = add.entry(width = 50 , row = 3 , column = 2 , padx = (0,0) , pady = (5,0))

    amount_label = add.label(text = 'จำนวน' , row = 4 , column = 0 , columnspan = 2 , padx = (0,0) , pady =(5,0))
    amount_entry = add.entry(width = 50 , row = 4 , column = 2 , padx = (0,0) , pady = (5,0))
    
    price_label = add.label(text = 'ราคา' , row = 5 , column = 0 , columnspan = 2 , padx = (0,0) , pady =(5,0))
    price_entry = add.entry(width = 50 , row = 5 , column = 2 , padx = (0,0) , pady = (5,0))

    confirm_button = add.button(text = 'เพิ่มรายการสินค้า' , row = 6 , column = 0 , columnspan = 3 , padx = (0,0) , pady = (10,0) , command = addList)

def showStockList() :
    clearScreen()
    def showList(choice = '') :
        data = api.data.get()
        for i in range (len(data)) :
            if (data[i]['Name'] == name_optionMenu['text']) :
                description_text['text'] = data[i]['Description']
                price_amount['text'] = data[i]['Price']
                remain_amount['text'] = data[i]['Amount']
                break

    showList_label = add.label(text = 'รายการสินค้าในระบบ' , row = 1 , column = 2 , padx = (0,0) , pady = (0,0))

    options = api.readData.name()

    name_label = add.label(text = 'ชื่อสินค้า' , row = 2 , column = 0 , columnspan = 2 , padx = (0,0) , pady = (10,0))
    name_optionMenu = add.optionMenu(text = 'เลือกสินค้า' , options = options , row = 2 , column = 2 , padx = (0,0) , pady = (10,0) , command = showList)

    description_label = add.label(text = 'คำอธิบายสินค้า' , row = 3 , column = 0 , columnspan = 2 , padx = (0,0) , pady =(5,0))
    description_text = add.label(text = 'เลือกสินค้าเพื่อแสดงรายละเอียดสินค้า' , row = 3 , column = 2 , padx = (0,0) , pady = (5,0))

    price_label = add.label(text = 'ราคา' , row = 4 , column = 0 , columnspan = 2 , padx = (0,0) , pady =(5,0))
    price_amount = add.label(text = '-' , row = 4 , column = 2 , padx = (0,0) , pady = (5,0))

    remain_label = add.label(text = 'สินค้าคงเหลือ' , row = 5 , column = 0 , columnspan = 2 , padx = (0,0) , pady =(5,0))
    remain_amount = add.label(text = '-' , row = 5 , column = 2 , padx = (0,0) , pady = (5,0))

def editStockList() :
    clearScreen()
    def editList() :
        data = api.data.get()
        for i in range (len(data)) :
            if (data[i]['Name'] == name_optionMenu['text']) :
                api.data.put(data[i]['Name'] , description_entry.get() , data[i]['Amount'] , price_entry.get())
                break

    def showList(choice = '') :
        data = api.data.get()
        for i in range (len(data)) :
            if (data[i]['Name'] == name_optionMenu['text']) :
                description_entry.delete(0 , 'end')
                price_entry.delete(0 , 'end')
                description_entry.insert(0 , data[i]['Description'])
                price_entry.insert(0 , data[i]['Price'])
                break

    editList_label = add.label(text = 'แก้ไขรายการสินค้าในระบบ' , row = 1 , column = 2 , padx = (0,0) , pady = (0,0))

    options = api.readData.name()

    name_label = add.label(text = 'ชื่อสินค้า' , row = 2 , column = 0 , columnspan = 2 , padx = (0,0) , pady = (10,0))
    name_optionMenu = add.optionMenu(text = 'เลือกสินค้า' , options = options , row = 2 , column = 2 , padx = (0,0) , pady = (10,0) , command = showList)

    description_label = add.label(text = 'คำอธิบายสินค้า' , row = 3 , column = 0 , columnspan = 2 , padx = (0,0) , pady =(5,0))
    description_entry = add.entry(width = 50 , row = 3 , column = 2 , padx = (0,0) , pady = (5,0))
    description_entry.insert(0 , 'เลือกสินค้าเพื่อแสดงรายละเอียดสินค้า')

    price_label = add.label(text = 'ราคา' , row = 4 , column = 0 , columnspan = 2 , padx = (0,0) , pady =(5,0))
    price_entry = add.entry(width = 50 , row = 4 , column = 2 , padx = (0,0) , pady = (5,0))
    price_entry.insert(0 , '-')

    confirm_button = add.button(text = 'แก้ไขรายการสินค้า' , row = 5 , column = 0 , columnspan = 3 , padx = (0,0) , pady = (10,0) , command = editList)

def removeStockList() :
    clearScreen()
    def removeList() :
        data = api.data.get()
        for i in range (len(data)) :
            if (data[i]['Name'] == name_optionMenu['text']) :
                try:
                    api.data.delete(data[i]['Name'] , data[i]['Description'] , data[i]['Amount'] , data[i]['Price'] , data[i]['Date'] , data[i]['Time'])
                except:
                    removeStockList()

    def showList(choice = '') :
        data = api.data.get()
        for i in range (len(data)) :
            if (data[i]['Name'] == name_optionMenu['text']) :
                description_text['text'] = data[i]['Description']
                price_amount['text'] = data[i]['Price']
                remain_amount['text'] = data[i]['Amount']
                break
        
    removeList_label = add.label(text = 'ลบรายการสินค้าในระบบ' , row = 1 , column = 2 , padx = (0,0) , pady = (0,0))

    options = api.readData.name()

    name_label = add.label(text = 'ชื่อสินค้า' , row = 2 , column = 0 , columnspan = 2 , padx = (0,0) , pady = (10,0))
    name_optionMenu = add.optionMenu(text = 'เลือกสินค้าที่ต้องการลบ' , options = options , row = 2 , column = 2 , padx = (0,0) , pady = (10,0) , command = showList)

    description_label = add.label(text = 'คำอธิบายสินค้า' , row = 3 , column = 0 , columnspan = 2 , padx = (0,0) , pady =(5,0))
    description_text = add.label(text = 'เลือกสินค้าเพื่อลบออกจากรายการสินค้า' , row = 3 , column = 2 , padx = (0,0) , pady = (5,0))

    price_label = add.label(text = 'ราคา' , row = 4 , column = 0 , columnspan = 2 , padx = (0,0) , pady =(5,0))
    price_amount = add.label(text = '-' , row = 4 , column = 2 , padx = (0,0) , pady = (5,0))

    remain_label = add.label(text = 'สินค้าคงเหลือ' , row = 5 , column = 0 , columnspan = 2 , padx = (0,0) , pady =(5,0))
    remain_amount = add.label(text = '-' , row = 5 , column = 2 , padx = (0,0) , pady = (5,0))

    confirm_button = add.button(text = 'ลบรายการสินค้า' , row = 6 , column = 0 , columnspan = 3 , padx = (0,0) , pady = (10,0) , command = removeList)

def buyGoods() :
    clearScreen()
    def addGoods() :
        data = api.data.get()
        for i in range (len(data)) :
            if (data[i]['Name'] == name_optionMenu['text']) :
                try :
                    api.data.goods.buy(data[i]['Name'] , data[i]['Description'] , amount_entry.get() , data[i]['Price'])
                except :
                    showList()

    def showList(choice = '') :
        data = api.data.get()
        for i in range (len(data)) :
            if (data[i]['Name'] == name_optionMenu['text']) :
                amount_entry.delete(0 , 'end')
                description_text['text'] = data[i]['Description']
                remain_amount['text'] = data[i]['Amount']
                break

    buy_label = add.label(text = 'สั่งซื้อสินค้า' , row = 1 , column = 2 , padx = (0,0) , pady = (0,0))

    options = api.readData.name()

    name_label = add.label(text = 'ชื่อสินค้า' , row = 2 , column = 0 , columnspan = 2 , padx = (0,0) , pady = (10,0))
    name_optionMenu = add.optionMenu(text = 'เลือกสินค้า' , options = options , row = 2 , column = 2 , padx = (0,0) , pady = (10,0) , command = showList)

    description_label = add.label(text = 'คำอธิบายสินค้า' , row = 3 , column = 0 , columnspan = 2 , padx = (0,0) , pady =(5,0))
    description_text = add.label(text = 'เลือกสินค้าเพื่อแสดงรายละเอียดสินค้า' , row = 3 , column = 2 , padx = (0,0) , pady = (5,0))

    remain_label = add.label(text = 'สินค้าคงเหลือ' , row = 4 , column = 0 , columnspan = 2 , padx = (0,0) , pady =(5,0))
    remain_amount = add.label(text = '-' , row = 4 , column = 2 , padx = (0,0) , pady = (5,0))

    amount_label = add.label(text = 'จำนวนที่สั่งซื้อ' , row = 5 , column = 0 , columnspan = 2 , padx = (0,0) , pady =(5,0))
    amount_entry = add.entry(width = 50 , row = 5 , column = 2 , padx = (0,0) , pady = (5,0))

    confirm_button = add.button(text = 'เพิ่มสินค้า' , row = 6 , column = 0 , columnspan = 3 , padx = (0,0) , pady = (10,0) , command = addGoods)

def sellGoods() :
    clearScreen()
    def sellGoods() :
        data = api.data.get()
        for i in range (len(data)) :
            if (data[i]['Name'] == name_optionMenu['text']) :
                try :
                    api.data.goods.sell(data[i]['Name'] , data[i]['Description'] , amount_entry.get() , data[i]['Price'])
                except :
                    showList()

    def showList(choice = '') :
        data = api.data.get()
        for i in range (len(data)) :
            if (data[i]['Name'] == name_optionMenu['text']) :
                amount_entry.delete(0 , 'end')
                description_text['text'] = data[i]['Description']
                remain_amount['text'] = data[i]['Amount']
                price_amount['text'] = data[i]['Price']
                break

    sell_label = add.label(text = 'ขายซื้อสินค้า' , row = 1 , column = 2 , padx = (0,0) , pady = (0,0))

    options = api.readData.name()

    name_label = add.label(text = 'ชื่อสินค้า' , row = 2 , column = 0 , columnspan = 2 , padx = (0,0) , pady = (10,0))
    name_optionMenu = add.optionMenu(text = 'เลือกสินค้า' , options = options , row = 2 , column = 2 , padx = (0,0) , pady = (10,0) , command = showList)

    description_label = add.label(text = 'คำอธิบายสินค้า' , row = 3 , column = 0 , columnspan = 2 , padx = (0,0) , pady =(5,0))
    description_text = add.label(text = 'เลือกสินค้าเพื่อแสดงรายละเอียดสินค้า' , row = 3 , column = 2 , padx = (0,0) , pady = (5,0))

    remain_label = add.label(text = 'สินค้าคงเหลือ' , row = 4 , column = 0 , columnspan = 2 , padx = (0,0) , pady =(5,0))
    remain_amount = add.label(text = '-' , row = 4 , column = 2 , padx = (0,0) , pady = (5,0))

    price_label = add.label(text = 'ราคา' , row = 5 , column = 0 , columnspan = 2 , padx = (0,0) , pady =(5,0))
    price_amount = add.label(text = '-' , row = 5 , column = 2 , padx = (0,0) , pady = (5,0))

    amount_label = add.label(text = 'จำนวนที่ขาย' , row = 6 , column = 0 , columnspan = 2 , padx = (0,0) , pady =(5,0))
    amount_entry = add.entry(width = 50 , row = 6 , column = 2 , padx = (0,0) , pady = (5,0))

    confirm_button = add.button(text = 'ขายสินค้า' , row = 7 , column = 0 , columnspan = 3 , padx = (0,0) , pady = (10,0) , command = sellGoods)

def clearScreen() :
    excel.data.updateExcel()
    for widget in frame.winfo_children() :
        widget.destroy()

#ปรับการตั้งค่าโปรแกรม
app = tk.Tk()
app.title('FirstClassCoding')
app.geometry('500x400') # app.resizable(0,0)
icon = tk.PhotoImage(file = './database/FirstClassCoding_LOGO.png')
app.iconphoto(False,icon)

menuBar = tk.Menu(master = app)

frame = tk.Frame(app)
frame.grid(row = 0 , column = 0)

#Stock Menu
menu_Stock = tk.Menu(master = menuBar , tearoff = 0)
menu_Stock.add_command(label = 'สั่งสินค้า' , command = buyGoods)
menu_Stock.add_command(label = 'ขายสินค้า' , command = sellGoods)
menu_Stock.add_separator()
menu_Stock.add_command(label = 'เรียกดูรายการสินค้า' , command = showStockList)
menu_Stock.add_command(label = 'เพิ่มรายการสินค้า' , command = addStockList)
menu_Stock.add_command(label = 'แก้ไขรายการสินค้า' , command = editStockList)
menu_Stock.add_command(label = 'ลบรายการสินค้า' , command = removeStockList)
menuBar.add_cascade(label = 'สินค้า' , menu = menu_Stock)

runThread = threading.Thread(target = runTime)
runThread.start()

app.config(menu = menuBar)
app.mainloop()
