import requests
from getTime import getTime

class data :
    class goods :
        def buy(name = '' , description = '' , amount = '' , price = '') :
            sendData = { 'listData': {
            'name': name,
            'description': description,
            'amount': amount,
            'price': price }}

            requests.put('http://127.0.0.1:3000/data/buygoods', json = sendData, timeout = 0.1)

        def sell(name = '' , description = '' , amount = '' , price = '') :
            sendData = { 'listData': {
            'name': name,
            'description': description,
            'amount': amount,
            'price': price }}

            requests.put('http://127.0.0.1:3000/data/sellgoods', json = sendData, timeout = 0.1)

    def get() :
        res = requests.get('http://127.0.0.1:3000/data')
        data = res.json()
        return data

    def post(name = '' , description = '' , amount = '' , price = '') :
        sendData = { 'listData': {
        'name': name,
        'description': description,
        'amount': amount,
        'price': price }}

        requests.post('http://127.0.0.1:3000/data', json = sendData, timeout = 0.1)

    def put(name = '' , description = '' , amount = '' , price = '') :
        sendData = { 'listData': {
        'name': name,
        'description': description,
        'amount': amount,
        'price': price }}

        requests.put('http://127.0.0.1:3000/data', json = sendData, timeout = 0.1)

    def delete(name = '' , description = '' , amount = '' , price = '' , date = '' , time = '') :
        sendData = { 'listData': {
        'name': name,
        'description': description,
        'amount': amount,
        'price': price,
        'date': date,
        'time': time }}

        requests.delete('http://127.0.0.1:3000/data', json = sendData, timeout = 0.1)

class readData :
    def name() :
        getData = data.get()
        sendData = []
        for i in range (len(getData)) :
            sendData.append(getData[i]['Name'])
        return sendData