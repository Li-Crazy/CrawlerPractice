import requests

def query():
    response = requests.get('https://kyfw.12306.cn/otn/leftTicket/queryX'
                            '?leftTicketDTO.train_date=2019-03-16&leftTicketDTO.from_station=CSQ'
                            '&leftTicketDTO.to_station=CDW&purpose_codes=ADULT')

    return response.json()['data']['result']


for i in query():
    tem_list = i.split('|')
    j = 0
    for n in tem_list:
        print(j,n)
        j += 1