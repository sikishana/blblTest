import json


import requests

from proIni import opIO, closeIO, rwTime
from timeTrans import timeTrans


# dict:url集合
# 判断后返回的结果
def dealLottery(dict, token):
    #打开io流
    cfp = opIO()
    #x：key str：value
    for x, str in dict.items():
        if str != '':
            s = requests.get(url=str)
            js_dict = json.loads(s.text)
            if 'data' not in js_dict:
                continue
            if s.status_code == 200:
                print(js_dict['data'][0])
                # 最新一条获奖记录
                target = js_dict['data'][0]
                # 活动名称
                active_name = target['award_info']['activity_name']
                # 中奖人
                gift_owner = target['name']
                # 中奖奖品
                gift_name = target['gift_name']
                # 中奖时间
                c_time = timeTrans(target['ctime'])
                # 中奖时间戳
                lottery_ts = target['ctime']

                msg_return = '时间:' + c_time + '\n' + ' 货:' + gift_name + '\n' + 'U:' + gift_owner

                if rwTime(cfp, x, lottery_ts):
                    print('success')
                    print('title:' + active_name + x)
                    print('content:' + msg_return)
                    print('================')
                    requests.get('http://www.pushplus.plus/send/f6be2c66b99d4e78bd1811bc80814d79',
                        params={'title': x+active_name,
                                'content': msg_return}
                    )
                else:
                    print('活动名：' + active_name + x)
                    print('出货人：' + gift_name)
                    print('出货时间：' + c_time)
                    print('-------------------------')


    print('end=======================================================end')
    closeIO(cfp)

