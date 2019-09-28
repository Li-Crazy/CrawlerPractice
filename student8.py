import requests
import json

class FanYi():
    def __init__(self,query_string):
        self.query_string = query_string
        self.url = "https://fanyi.baidu.com/transapi"
        self.headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)" 
                        "Chrome/70.0.3538.25 Safari/537.36"}
    def type_string(self):
        if self.query_string.encode().isalpha():
            return {
                "from": "en",
                "to": "zh"
            }
        else:
            return {
                "from": "zh",
                "to": "en"
            }


    def get_post_data(self):
        post_data = {
            "query": self.query_string
        }
        post_data.update(self.type_string())
        return post_data


    def parse_url(self,url,data):
        response = requests.post(url,data=data,headers=self.headers)
        return response.content.decode()

    def get_data(self,json_str):
        dict_data = json.loads(json_str)
        data = dict_data["data"][0]["dst"]
        print("{}:{}".format(self.query_string,data))




    def run(self):
        post_data = self.get_post_data()
        json_str = self.parse_url(self.url,post_data)
        self.get_data(json_str)




if __name__ == '__main__':
    print("-" * 100)
    print("+" * 35+"支持汉译英，以及单个单词的翻译"+"+" * 35)
    print("-" * 100)

    while True:
        try:
            get_data = input("请输入你要翻译的内容：")
            fanyi = FanYi(get_data)
            fanyi.run()
        except Exception as KeyError:
            print("您的输入有误，程序自动退出……")
            break

