import requests
import json
import time
import math

# 获取国家列表
def country():
    
    url='https://www.yidaiyilu.gov.cn/dataChart'
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.69'
    }
    params = {
    }
    # 数据在在script里面，在页面上可以使用window._NUXT_.data[0].countryList获取
    text= requests.get(url,params=params,headers=headers).text
    return text


