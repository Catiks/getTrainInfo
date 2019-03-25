# -*- coding: utf-8 -*-
import codecs
import urllib
from urllib import request
import requests
import re

#关闭https证书验证警告
requests.packages.urllib3.disable_warnings()
if __name__ == '__main__':

    requests.packages.urllib3.disable_warnings()
    outfile = codecs.open('station_code.json', 'w', 'utf-8')
    # 12306的城市名和城市代码js文件url
    url = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9018'
    r = requests.get(url, verify=False)
    pattern = u'([\u4e00-\u9fa5]+)\|([A-Z]+)'
    result = re.findall(pattern, r.text)
    station = dict(result)

    outfile.write(str(station))
    print(len(station))
    outfile.close()

'''
查询两站之间的火车票信息
输入参数： <date> <from> <to>
12306 api:
'https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2017-07-18&leftTicketDTO.from_station=NJH&leftTicketDTO.to_station=SZH&purpose_codes=ADULT'
'''
