import urllib.request
import yaml


def request():
    try:
        url = "http://rapid-hub.org/data/angles_UCI_CS.csv"
        http_response = urllib.request.urlopen(url)
    except ConnectionError:
        print("[-] Failed to retrieve from website")

    data = yaml.load(http_response).split(' ')
    print(data)
    #[{station_id: 0, angles_degrees: 90}, {}]
    print("station_id angle_degrees")
    for value in data[2:]:
        print(value)


if __name__ == '__main__':
    request()
