import requests
from pythonping import ping

massages = [{"U": 2}, {"B": 2}, {"L": 2}, {"R": 2}, {"S": 2}, {"T": 2}]
conn_timeout = 0.05
read_timeout = 0.05
timeouts = (conn_timeout, read_timeout)
checkValue = 0
Avg_ms = '0'
Max_ms = '0'
Min_ms = '0'


def moveRobot(order, address='0'):
    global checkValue
    if order == 1:
        print('Forward')
        try:
            requests.post(address, params=massages[0], timeout=timeouts)
        except requests.Timeout:
            print('Receiving Signals')
        except requests.ConnectionError:
            print('Connection Error')

    elif order == 2:
        print('Backward')
        try:
            requests.post(address, params=massages[1], timeout=timeouts)
        except requests.Timeout:
            print('Receiving Signals')
        except requests.ConnectionError:
            print('Connection Error')
    elif order == 3:
        print('Left')
        try:
            requests.post(address, params=massages[2], timeout=timeouts)
        except requests.Timeout:
            print('Receiving Signals')
        except requests.ConnectionError:
            print('Connection Error')
    elif order == 4:
        print('Right')
        try:
            requests.post(address, params=massages[3], timeout=timeouts)
        except requests.Timeout:
            print('Receiving Signals')
        except requests.ConnectionError:
            print('Connection Error')
    elif order == 5:
        print('Stopped')
        try:
            requests.post(address, params=massages[4], timeout=timeouts)
        except requests.Timeout:
            print('Receiving Signals')
        except requests.ConnectionError:
            print('Connection Error')
    elif order == 6:
        print('Scanning')
        try:
            requests.post(address, params=massages[5], timeout=timeouts)
        except requests.Timeout:
            checkValue = 1
            print('Connection Established')
        except requests.ConnectionError:
            checkValue = 0
    else:
        print('Wrong Command')
        try:
            requests.post(address, params=massages[4], timeout=timeouts)
        except requests.Timeout:
            print('Receiving Signals')
        except requests.ConnectionError:
            print('Connection Error')


def pingTest(url):
    global Avg_ms, Max_ms, Min_ms
    Test = ping(url, count=1, size=100)
    Avg_ms = Test.rtt_avg_ms
    Max_ms = Test.rtt_max_ms
    Min_ms = Test.rtt_min_ms
