import urllib.request


def request():
    try:
        url = "http://rapid-hub.org/data/angles_UCI_CS.csv"
        http_response = urllib.request.urlopen(url)
    except ConnectionError:
        print("[-] Failed to retrieve from website")

    print(http_response.read().decode('utf-8'))


if __name__ == '__main__':
    request()
