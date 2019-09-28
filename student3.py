from aip import AipSpeech
# from aip import AipOcr

APP_ID = '15770042'
API_KEY = 'R5RLYHV5R54R50VUFR2XE2TG'
SECRET_KEY = 'qFCN4BqABxQzg6HLYgcTZuqixhXqMpnE'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)


result = client.synthesis( """我王某人头铁，从不救队友""",'zh',1,{
                "vol":5,   #音量，取值0-15，默认为5中音量
                "spd":6,	#	语速，取值0-9，默认为5中语速
                "pit":6,	#	音调，取值0-9，默认为5中语调
                "per":4,	#	发音人选择, 0为女声，1为男声，3为情感合成-度逍遥，4为情感合成-度丫丫，默认为普通女
            })
print(result)
if not isinstance(result, dict):
    with open("audio.mp3","wb") as f:
        f.write(result)

# from aip import AipSpeech
#
# APP_ID = '15770042'
# API_KEY = 'R5RLYHV5R54R50VUFR2XE2TG'
# SECRET_KEY = 'qFCN4BqABxQzg6HLYgcTZuqixhXqMpnE'
#
# client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
#
# result = client.synthesis("""
# 轻轻的我走了，
# 正如我轻轻的来；
# 我轻轻的招手，
# 作别西天的云彩。 """, 'zh', 1, {
#
#     'vol': 5,#音量，取值0-15，默认为5中音量
#     'spd':6,# 语速，取值0-9，默认为5中语速
#     "pit":6,#音调，取值0-9，默认为5中语调
#     "per":4,#发音人选择, 0为女声，1为男声，3为情感合成-度逍遥，4为情感合成-度丫丫，默认为普通女
# })
# print(result)
# # 识别正确返回语音二进制 错误则返回dict 参照下面错误码
# if not isinstance(result, dict):
#     with open('auido.mp3', 'wb') as f:
#         f.write(result)
