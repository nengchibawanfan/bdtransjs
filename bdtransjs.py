import urllib.request
import urllib.parse
import json

url = "http://fanyi.baidu.com/v2transapi"

headers = {
    "Accept": "*/*",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Host": "fanyi.baidu.com",
    "Origin": "http://fanyi.baidu.com",
    "Pragma": "no-cache",
    "Referer": "http://fanyi.baidu.com/",
    "X-Requested-With": "XMLHttpRequest",
    'Cookie': 'BAIDUID=256C72EF575B148C1E5672FBEBB2B072:FG=1; PSTM=1532575058; BIDUPSID=25B2CBDECE1643A45F149D48681E7E7C; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; to_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; locale=zh; from_lang_often=%5B%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22it%22%2C%22text%22%3A%22%u610F%u5927%u5229%u8BED%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D; PSINO=1; H_PS_PSSID=26937_1428_21119_26350_26921_22072; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1531330412,1532097434,1533591486,1533595389; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1533595389',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36',

}

import execjs

inputData = "python"

with open("bd.js") as f:
    jsData = f.read()

p = execjs.compile(jsData).call("e", inputData)

formData = {
    "from": "en",
    "to": "zh",
    "query": inputData,
    "transtype": "realtime",
    "simple_means_flag": "3",
    "sign": p,
    "token": "c6494eba8aef403bf04ba17ff6114014",
}

data=urllib.parse.urlencode(formData).encode("utf-8")
request = urllib.request.Request(url=url, data=data, headers=headers)

print(json.loads(urllib.request.urlopen(request).read().decode("utf-8")))