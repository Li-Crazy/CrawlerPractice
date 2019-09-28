import requests # 模拟发送网络请求库
import base64 # bs64数据类型库
import json # json数据类型库

api1 = "https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=vUG5H0WV9xwerDmXCgxsksUs&client_secret=Im60eyc4OG61F6rFumi5SBMteEeZZgWb"
#'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=【百度云应用的AK】&client_secret=【百度云应用的SK】'
# 1. 获取token值 拼接API
def get_token():
    response = requests.get(api1)#发送网络请求
    access_token = eval(response.text)['access_token']#获取access_token值
    api2 = "https://aip.baidubce.com/rest/2.0/face/v3/match?access_token=" + access_token#拼接api 人脸对比
    #https://aip.baidubce.com/rest/2.0/face/v3/match?access_token=24.f9ba9c5341b67688ab5added8bc91dec.2592000.1485570332.282335-8574075
    return api2

# 2. 读取图片数据
def img(img1, img2):
    with open(img1, "rb") as f:#读取二进制数据
        pic1 = base64.b64encode(f.read())#二进制编码转化为base64数据，接口需要
    with open(img2, "rb") as f:
        pic2 = base64.b64encode(f.read())

    params = json.dumps([#整合成json类型
        {"image": str(pic1, "utf-8"), "image_type": "BASE64", "face_type": "LIVE", "quality_control": "LOW"},
        {"image": str(pic2, "utf-8"), "image_type": "BASE64", "face_type": "IDCARD", "quality_control": "LOW"},
    ])#字典数据类型存储图片数据
    #"image": str(pic1, "utf-8"),转换为字符串类型
    #"image_type": "BASE64",图片类型
    #"face_type": "LIVE",脸部类型，生活照，证件照
    return params

# 3. 发送请求拿到对比结果
def than_img(file1, file2):#图片比较方法
    params = img(file1, file2)
    api = get_token()
    content = requests.post(api, params).text#请求api，对图片进行比较
    score = eval(content)['result']['score']#获得相似百分比，转化为Python数据

    if score > 80:
        print("图片相似度：" + str(score) + ",同一个人")
    else:
        print("图片相似度：" + str(score) + ",不是同一个人")


than_img("C:/Users/19845/Desktop/123.jpg", "C:/Users/19845/Desktop/1.jpg")

