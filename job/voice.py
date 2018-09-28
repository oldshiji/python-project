

'''
from aip import AipSpeech

""" 你的 APPID AK SK """
APP_ID = '10844944'
API_KEY = 'nu16KzgFTs7NXuahTGlWr9Ge'
SECRET_KEY = 'd03ba853038ad372ea0a473cd920c863'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

result  = client.synthesis('你的账户已经充值十万吨黄金了主人', 'zh', 1, {
    'vol': 5,
    'per':4,
    'pit':4
})
pit	String	音调，取值0-9，默认为5中语调	否
vol	String	音量，取值0-15，默认为5中音量	否
per	String	发音人选择, 0为女声，1为男声，
3为情感合成-度逍遥，4为情感合成-度丫丫，默认为普通女	否

# 识别正确返回语音二进制 错误则返回dict 参照下面错误码
if not isinstance(result, dict):
    with open('auido1.mp3', 'wb') as f:
        f.write(result)
'''


from translate import Translator
translator= Translator(to_lang="en",from_lang="zh")
translation = translator.translate("标题")
print(translation)