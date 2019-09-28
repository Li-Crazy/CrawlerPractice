import requests
import re

#定义第一个函数 目的：获取分类里的小说
def get_novel_list():
    #请求的是分类的url
    response=requests.get('http://www.quanshuwang.com/list/1_1.html')
    response.encoding = 'gbk'
    html = response.text
    #用正则表达式来匹配每一部小说的Url
    #.*表示匹配任意数量不换行的字符？
    reg = r'<a target="_blank" href="(.*?)" class="1 mr10">'
    #print(re.findall(reg,html))
    return re.findall(reg,html)

#定义第二个函数 目的：获取章节列表的内容
def get_chapter_list(novel_url):

    #请求分类里对应小说的Url
    response = requests.get(novel_url)
    response.encoding = 'gbk'
    html = response.text
    #匹配每部小说所对应的开始阅读
    reg = r'<a href="(.*?)" class="reader">'
    #print(re.findall(reg, html)[0])
    chapter_list_url = re.findall(reg,html)[0]
    #请求章节列表所对应的url
    response = requests.get(chapter_list_url)
    response.encoding = 'gbk'
    html = response.text
    reg = r'<li><a href = "(.*?)" title = ".*?">(.*?)</a></li> '

    #print(re.findall(reg,html))
    return re.findall(reg,html)
#定义第三个函数 目的：获取小说内容
def get_chapter_content(chapter_url):
    response = requests.get(chapter_url)
    response.encoding='gbk'
    html = response.text
    #匹配每部小说对应内容
    reg = r'style5\(\);</script>(.*?)<script type="text/javascript">style6\(\)'
    #print(re.findall(reg,html,re.S)[0])
    return re.findall(reg,html,re.S)[0]


for novel_url in get_novel_list():

    for chapter_url,chapter_name in get_chapter_list(novel_url):
        #print(i)
        #chapter_url = i[0]
        #chapter_name = i[1]
        # print(chapter_url)
        # print(chapter_name)
        chapter_content = get_chapter_content(chapter_url)
        #保存文件
        fn = open(chapter_name + '.html','w')
        fn.write(chapter_content)
        fn.close()
        #break
    break#不需要每个链接都打开

    #print(novel_url)