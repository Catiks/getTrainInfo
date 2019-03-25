# -*- coding: utf-8 -*-
import codecs
import json

if __name__ == '__main__':
    js = codecs.open('train_list', 'r', 'utf-8')
    data = js.read()
    jsondata = json.loads(data.strip('var train_list ='))
    print(jsondata['2019-04-01']['T'])
