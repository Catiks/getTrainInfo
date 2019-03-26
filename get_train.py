# -*- coding: utf-8 -*-
import codecs
import json

if __name__ == '__main__':
    js = codecs.open('train_list', 'r', 'utf-8')
    out = codecs.open('train_list.json','w', 'utf-8')
    data = js.read()
    jsondata = json.loads(data.strip('var train_list ='))
    out.write(json.dumps(jsondata, ensure_ascii=False))
    js.close()
    out.close()

