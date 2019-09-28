import requests
import re

def get_urls():
    response = requests.get('https://qq.yh31.com/zjbq/2378278.html')
    url_add = r'<img src="(.*?)"'
    url_list = re.findall(url_add,response.text)
    return url_list


def get_gif(url,name):
    response = requests.get(url)

    with open('photo\%d.gif'% name,'wb') as ft:
        ft.write(response.content)




if __name__ == '__main__':
    url_list = get_urls()
    a = 1
    for url in url_list:
        com_url = 'https://qq.yh31.com/'+ url
        get_gif(com_url,a)
        a += 1
        print(com_url)