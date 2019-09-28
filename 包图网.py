import requests
from lxml import etree


response = requests.get("https://ibaotu.com/shipin/")


xml = etree.HTML(response.text)
tit_list = xml.xpath('//span[@class="video-title"]/text()')
src_list = xml.xpath('//div[@class="video-play"]/video/@src')

for tit,src in zip (tit_list,src_list):

    response = requests.get("http:" + src)
    fileName = "video\\" + tit + ".mp4"
    print("正在保存小视频："+ fileName)

    with open(fileName, "wb") as f:
        f.write(response.content)

