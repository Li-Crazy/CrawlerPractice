import json

import pygal
import requests

# json_url = "https://raw.githubusercontent.com/muxuezi/btc/master/btc_close_2017.json"


# response = requests.get(json_url)

# print(response.text)
# with open("gs.json","w") as f:
#     f.write(response.text)
#
# file_requests = response.json()

file_name = "gs.json"
with open(file_name) as f:
    gs_data = json.load(f)
    # print(gs_data)
datas = []
months = []
weeks = []
weekdays = []
closes = []

for gs_data in gs_data:
    datas.append(gs_data["date"])
    months.append(gs_data["month"])
    weeks.append(gs_data["week"])
    weekdays.append(gs_data["weekday"])
    closes.append(float(gs_data["close"]))

view = pygal.Line()
view.title = "收盘价（￥）"
view.x_labels = datas
view.add("收盘价",closes)
view.render_in_browser()