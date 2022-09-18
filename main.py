# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#02版本
from dealGet import dealLottery
import time

lottery_dict = {'2': 'https://api.bilibili.com/x/lottery/win/list?sid=newLottery_b8628b8c-1472-11ed-9251-a4ae12675bc2',
                '3': 'https://api.bilibili.com/x/lottery/win/list?sid=newLottery_bc4ea594-038f-11ed-9251-a4ae12675bc2',
                '4': 'https://api.bilibili.com/x/lottery/win/list?sid=newLottery_6cbb9e93-0e65-11ed-9251-a4ae12675bc2',
                '5': 'https://api.bilibili.com/x/lottery/win/list?sid=newLottery_a8143e38-1a25-11ed-9251-a4ae12675bc2',
                '6': 'https://api.bilibili.com/x/lottery/win/list?sid=newLottery_25717e23-1a39-11ed-9251-a4ae12675bc2',
                '7': 'https://api.bilibili.com/x/lottery/win/list?sid=newLottery_871a2f12-1303-11ed-9251-a4ae12675bc2',
                '8': 'https://api.bilibili.com/x/lottery/win/list?sid=newLottery_b2b57e6d-0ff6-11ed-9251-a4ae12675bc2',
                '9': 'https://api.bilibili.com/x/lottery/win/list?sid=newLottery_fbdfdfa4-0369-11ed-9251-a4ae12675bc2',
                '10': 'https://api.bilibili.com/x/lottery/win/list?sid=newLottery_3c4f311a-041b-11ed-9251-a4ae12675bc2',
                '11': 'https://api.bilibili.com/x/lottery/win/list?sid=newLottery_db7ebc39-0e22-11ed-9251-a4ae12675bc2',
                '12': '',
                '13': 'https://api.bilibili.com/x/lottery/win/list?sid=newLottery_604fce9f-09ad-11ed-9251-a4ae12675bc2',
                '14': 'https://api.bilibili.com/x/lottery/win/list?sid=newLottery_8a045973-125e-11ed-9251-a4ae12675bc2',
                '15': '',
                '16': 'https://api.bilibili.com/x/lottery/win/list?sid=newLottery_82b707a4-0c11-11ed-9251-a4ae12675bc2',
                '17': '',
                '18': 'https://api.bilibili.com/x/lottery/win/list?sid=newLottery_8b3e37a8-e30f-11ec-9251-a4ae12675bc2',
                '19': 'https://api.bilibili.com/x/lottery/win/list?sid=newLottery_0444c4a9-f6c0-11ec-9251-a4ae12675bc2',
                '20': 'https://api.bilibili.com/x/lottery/win/list?sid=newLottery_c71a6dc1-03fa-11ed-9251-a4ae12675bc2',
                '21': '',
                '22': 'https://api.bilibili.com/x/lottery/win/list?sid=newLottery_c02888c9-0354-11ed-9251-a4ae12675bc2',
                '23': '',
                '24': 'https://api.bilibili.com/x/lottery/win/list?sid=newLottery_60a7c37f-ee2d-11ec-9251-a4ae12675bc2',
                '25': '',
                '26': '',
                '27': 'https://api.bilibili.com/x/lottery/win/list?sid=newLottery_42983102-d5be-11ec-9251-a4ae12675bc2',
                '28': 'https://api.bilibili.com/x/lottery/win/list?sid=newLottery_6bf6c7c8-e564-11ec-9251-a4ae12675bc2',
                '29': '',
                '30': '',
                '31': '',
                '32': '',
                '40': 'https://api.bilibili.com/x/lottery/win/list?sid=newLottery_a7e99cef-0f34-11ed-9251-a4ae12675bc2',
                '42': 'https://api.bilibili.com/x/lottery/win/list?sid=newLottery_6f4efceb-13a3-11ed-9251-a4ae12675bc2'
                }
false = 'false'
null = 'null'
token = 'http://www.pushplus.plus/send/f6be2c66b99d4e78bd1811bc80814d79'


if __name__ == '__main__':

    while True:
        time.sleep(10)
        dealLottery(lottery_dict,token)
    # requests.get('http://www.pushplus.plus/send/f6be2c66b99d4e78bd1811bc80814d79',
    #              params={'title': 'x + active_name',
    #                      'content': 'msg_return'}
    #              )
    # s = requests.get('https://api.bilibili.com/x/lottery/win/list?sid=newLottery_bc4ea594-038f-11ed-9251-a4ae12675bc2')
    # t = json.loads(s.text)
    # print(t)


