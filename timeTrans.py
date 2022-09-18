import time



def timeTrans(time_Lottery):
    time_TransAfter = time.localtime(time_Lottery)
    ctime = time.strftime("%Y-%m-%d %H:%M:%S", time_TransAfter)
    return ctime



