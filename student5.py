from aip import AipSpeech
import os

APP_ID = '15770042'
API_KEY = 'R5RLYHV5R54R50VUFR2XE2TG'
SECRET_KEY = 'qFCN4BqABxQzg6HLYgcTZuqixhXqMpnE'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

def convert(file,audio_name):
    with open(file,"r",encoding="utf-8") as file_object:
        contents = file_object.read()
        print("正在转换{}".format(file))
        while len(contents)>=2000:
            tmp = contents[:2000]
            result = client.synthesis(tmp,"zh",1,{
                "vol":5,   #音量，取值0-15，默认为5中音量
                "spd":4,	#	语速，取值0-9，默认为5中语速
                "pit":9,	#	音调，取值0-9，默认为5中语调
                "per":3,	#	发音人选择, 0为女声，1为男声，3为情感合成-度逍遥，4为情感合成-度丫丫，默认为普通女
            })
            contents = contents[2000:]
            # with open("{}.mp3".format("./txtaudio/{}".format(file)),"wb") as f:
            try:
                with open("{}.mp3".format(audio_name),"ab") as f:
                    f.write(result)
                    print("{}转换完成".format(audio_name))
            except:
                print("error")
if __name__ == '__main__':
    convert(file,audio_name)