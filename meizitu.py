import requests
from lxml import etree

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36",
    "referer": "https://www.mzitu.com/tag/ugirls/"
}

# 1. 请求妹子图拿到网站数据
response = requests.get("https://www.mzitu.com/tag/ugirls/")

# 2. 抽取想要数据 图片标题 图片链接
xml = etree.HTML(response.text) # 整理成xml文档对象
tit_list = xml.xpath('//img[@class="lazy"]/@alt')
src_list = xml.xpath('//img[@class="lazy"]/@data-original')
for tit, src in zip(tit_list, src_list):
    # 3. 下载图片
    response = requests.get(src, headers=headers)
    fileName = "phone\\" + tit + ".jpg"
    print("正在保存图片文件：" + fileName)
    # 4. 保存图片
    with open(fileName, "wb") as f:
        f.write(response.content)