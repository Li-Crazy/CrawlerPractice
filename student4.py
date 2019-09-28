import requests
# from lxml import etree
import os
import student5  #语音转换模块，在后面会讲，请先注释掉，否则报错

## python3.7 有点坑啊，装了lxml模块却没有etree，后来查资料用以下方法即可导入使用
import lxml.html
etree = lxml.html.etree

class Spider(object):
    def start_request(self):
        response = requests.get("https://www.qidian.com/all")
        html = etree.HTML(response.content.decode())
        Bigtit_list=html.xpath('//div[@class="book-mid-info"]/h4/a/text()')
        Bigsrc_list=html.xpath('//div[@class="book-mid-info"]/h4/a/@href')
        # print(Bigsrc_list)
        book_name = input("请输入您要爬取的书名（eg：凡人修仙传之仙界篇）：")
        for Bigsrc,Bigtit in zip(Bigsrc_list,Bigtit_list):
            if Bigtit in book_name  or book_name in Bigtit:
                if os.path.exists(Bigtit) == False:
                    os.mkdir(Bigtit)		##创建以小说名为名字的文件夹存储小说
                    print("目标文件夹已创建")
                self.xpath_data(Bigsrc,Bigtit)


    def xpath_data(self,Bigsrc,Bigtit):
        response = requests.get("https:"+Bigsrc)
        html = etree.HTML(response.content.decode())
        Littit_list = html.xpath('//ul[@class="cf"]/li/a/text()')
        Litsrc_list = html.xpath('//ul[@class="cf"]/li/a/@href')
        for Litsrc,Littit in zip(Litsrc_list,Littit_list):
            self.finally_file(Littit,Litsrc,Bigtit)

    def finally_file(self,tit,url,Bigtit):
        response = requests.get("http:"+url)
        html = etree.HTML(response.content.decode())
        content = "\n".join(html.xpath('//div[@class="read-content j_readContent"]/p/text()'))
        file_name = Bigtit + "\\" + tit +".txt"
        audio_name = Bigtit + "\\" + tit +".mp3"		#语音文件名称
        print("正在抓取文章：" + file_name)
        with open(file_name, "a", encoding="utf-8") as f:
            f.write(content)
        student5.convert(file_name,audio_name)		#调用转语音模块进行转换

if __name__ == '__main__':
    spider=Spider()
    spider.start_request()
