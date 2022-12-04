import json
import pandas as pd
from getTime import getTime

class data :
    def read() :
        readData = pd.read_excel('./database/Data.xlsx')
        return readData

    def add(name , description = '' , price = '0') :
        getData = pd.DataFrame({'Name' : [name] , 'Description' : [description] , 'Amount' : ['0'] , 'Price' : [price] , 'Date' : [getTime.date()] , 'Time' : [getTime.time()]})
        mergeData = [data.read() , getData]
        writeData = pd.concat(mergeData)
        saveData = pd.ExcelWriter('./database/Data.xlsx' , engine = 'xlsxwriter')
        writeData.to_excel(saveData , index = False)
        saveData.save()
        data.toJSON()

    def edit() :
        readData = data.read().set_index('Name')

    def remove(name) :
        readData = data.read().set_index('Name')
        newData = readData.drop(name)
        writeData = newData.reset_index(level = 'Name')
        saveData = pd.ExcelWriter('./database/Data.xlsx' , engine = 'xlsxwriter')
        writeData.to_excel(saveData , index = False)
        saveData.save()
        data.toJSON()

    def goods(name , amount) :
        readData = data.read()
        getAmount = int(readData.loc[readData['Name'] == name , 'Amount'])
        newAmount = getAmount + int(amount)
        readData.loc[readData['Name'] == name , 'Amount'] = newAmount
        writeData = readData
        saveData = pd.ExcelWriter('./database/Data.xlsx' , engine = 'xlsxwriter')
        writeData.to_excel(saveData , index = False)
        saveData.save()
        data.toJSON()

    def toJSON() :
        readData = data.read()
        readData.to_json('./database/Data.json')

    def readJSON() :
        # return pd.read_json('./database/Data.json') // bug in date format
        with open('./database/Data.json') as json_file:
            return json.load(json_file)

    def updateExcel() :
        readData = data.readJSON()
        writeData = pd.DataFrame(readData)
        saveData = pd.ExcelWriter('./database/Data.xlsx' , engine = 'xlsxwriter')
        writeData.to_excel(saveData , index = False)
        saveData.save()

class history :
    def readJSON() :
        with open('./database/History.json') as json_file:
            return json.load(json_file)

    def updateExcel() :
        readData = history.readJSON()
        writeData = pd.DataFrame(readData)
        saveData = pd.ExcelWriter('./database/History.xlsx' , engine = 'xlsxwriter')
        writeData.to_excel(saveData , index = False)
        saveData.save()