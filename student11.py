import requests
import re

def get_urls():
    response = requests.get('http://www.1ppt.com/moban/shangwu/')
    url_add = r'<a href="/ar(.*?)" target="_blank"'
    url_list = re.findall(url_add,response.text)
    return url_list
    # print(url_list)
# get_urls()
def get_url(url):

    #请求分类里对应小说的Url
    response = requests.get(url)
    #匹配每部小说所对应的开始阅读
    reg = r'<a href="http://ppt(.*?)" target="_blank"'
    url_list = re.findall(reg,response.text)
    return url_list


# def get_name(url):
#     response = requests.get(url)
#     reg = r'<h1>蓝色(.*?)</h1>'
#     name = re.findall(reg, response.text)
#     return name


def get_ppt(url,name):
    response = requests.get(url)
    with open('move\%d.zip'% name,'wb') as ft:
        ft.write(response.content)


if __name__ == '__main__':
    url_list = get_urls()
    a = 1
    for url in url_list:
        first_url = 'http://www.1ppt.com/ar'+ url
        # name = get_name(first_url)
        # print(name)
        second_list = get_url(first_url)
        for i in second_list:
            second_url = 'http://ppt'+ i
            print(second_url)
            get_ppt(second_url,a)
            a += 1
#         print(second_list)