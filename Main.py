import urllib.request
import math


def request():
    url = "http://rapid-hub.org/data/angles_UCI_CS.csv"
    http_response = urllib.request.urlopen(url)
    data = http_response.read().decode('utf-8').replace('\r', '').split('\n')[:-1]

    print(data[0])
    for info in data[1:]:
        datainfo = info.split(',')
        print('{data0}\t\t{data1}\t\t{data2}'.format(data0=datainfo[0], data1=datainfo[1], data2=math.cos(int(datainfo[1]))))


if __name__ == '__main__':
    request()
