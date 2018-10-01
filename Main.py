import urllib.request
import math


def request():
    try:
        url = "http://rapid-hub.org/data/angles_UCI_CS.csv"
        http_response = urllib.request.urlopen(url)
    except ConnectionError:
        print("[-] Failed to retrieve from website")

    data = http_response.read().decode('utf-8').replace('\r', '').split('\n')[:-1]

    print(data[0])
    for info in data[1:]:
        datainfo = info.split(',')
        print(datainfo[0], '\t\t\t', datainfo[1], '           ', math.cos(int(datainfo[1])))


if __name__ == '__main__':
    request()
