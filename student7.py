import json
import jsonpath
import pygal
import requests

response = requests.get("http://pg.qq.com/zlkdatasys/data_zlk_zlzx.json")

py_data = json.loads(response.text)

gun_name = jsonpath.jsonpath(py_data, "$..mc_94")[1:8]
gun_xinn = jsonpath.jsonpath(py_data, "$..ldtw_f2")[0:7]

data = []

for i in gun_xinn:
    data.append([int(i[0]['wl_45']),int(i[0]['sc_54']),int(i[0]['ss_d0']),int(i[0]['wdx_a7']),int(i[0]['zds_62'])])

rader_chart = pygal.Radar()
rader_chart.title = "步枪性能"
rader_chart.x_labels = ["威力","射程","射速","稳定性","子弹数"]
for n,d in zip(gun_name ,data):
    print(n,d)
    rader_chart.add(n,d)
rader_chart.render_to_file("gun.svg")