import urllib.request
import math


def request():
    try:
        url = "http://rapid-hub.org/data/angles_UCI_CS.csv"
        http_response = urllib.request.urlopen(url)
    except ConnectionError:
        print("[-] Failed to retrieve from website")

    data = http_response.read().decode('utf-8').replace('\r', '').split('\n')[:-1]
    print(data)
    print('------------')
    print(data[0])
    for info in data[1:]:
        bracket = info.split(',')
        print(bracket[0], '\t\t\t', bracket[1], '           ', math.cos(int(bracket[1])))


if __name__ == '__main__':
    request()
