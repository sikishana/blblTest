import configparser
#key：键 cop——time：时间戳

def opIO():
    cfp = configparser.ConfigParser()
    cfp.read('yoyo.ini')
    return cfp
#cfp：文件流，key：就是key，cop——time最新中奖的时间戳


def rwTime(cfp,key,cop_time):

    org_time = cfp.getint('title', key)
    if cop_time > org_time:
        cop_time = str(cop_time)

        cfp.set('title', key, cop_time)
        print('写入成功')
        return True
    else:
        print('time_like')
        return False

def closeIO(cfp):
    cfp.write(open('yoyo.ini', 'w'))

