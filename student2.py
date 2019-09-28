import requests
from lxml import etree
import os

class Spider(object):
    def start_request(self):
        response = requests.get('http://www.qidian.com/all')
        xml  = etree.HTML(response.text)
        Bigtit_list = xml.xpath('//div[@class="book-mid-info"]/h4/a/text()')
        Bigsrc_list = xml.xpath('//div[@class="book-mid-info"]/h4/a/@href')
        book_name = input("请输入您要爬取的书名：")
        for Bigtit,Bigsrc in zip(Bigtit_list,Bigsrc_list):
            if Bigtit in book_name  or book_name in Bigtit:
                if os.path.exists(Bigtit) == False:
                    os.mkdir(Bigtit)
                    print("目标文件夹已创建")
                self.next_file(Bigtit,Bigsrc)
    def next_file(self,Bigtit,Bigsrc):
        response = requests.get("http:"+Bigsrc)
        xml = etree.HTML(response.text)
        Littit_list = xml.xpath('//ul[@class="cf"]/li/a/text()')
        Litsrc_list = xml.xpath('//ul[@class="cf"]/li/a/@href')
        for Littit,Litsrc in zip(Littit_list,Litsrc_list):
           self.finally_file(Littit,Litsrc,Bigtit)

    def finally_file(self,Littit,Litsrc,Bigtit):
        response = requests.get("http:" + Litsrc)
        xml = etree.HTML(response.text)
        content = "\n".join(xml.xpath('//div[@class="read-content j_readContent"]/p/text()'))
        fileName = Bigtit + "\\" + Littit + ".txt"
        audioName = Bigtit + "\\" + Littit + ".mp3"
        print("正在保存文件："+ fileName)
        with open(fileName,"w",encoding="utf-8") as f:
            f.write(content)

if __name__ == '__main__':
    spider = Spider()
    spider.start_request()