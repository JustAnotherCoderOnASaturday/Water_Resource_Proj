import urllib.request
import yaml


def request():
    try:
        url = "http://rapid-hub.org/data/angles_UCI_CS.csv"
        http_response = urllib.request.urlopen(url)
    except ConnectionError:
        print("[-] Failed to retrieve from website")

    data = yaml.load(http_response)
    print(data)
    print('[+] Job Complete')


if __name__ == '__main__':
    request()
