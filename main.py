import requests
from secretsu import get_url


def get_hook_info(url):

    response = requests.get(url)
    return response.text


def send_message(url, msg):
    payload = {
        "content": msg
    }
    requests.post(url, json=payload)


def start():
    r = requests

    print('Choose WebHook')
    print('1 - Testing on klacek server')
    print('2 - Sharp on klacek server')
    print('3 - Sharp on Oskar server')

    dec = int(input('Enter number 1/2/3> '))
    url = get_url(dec)
    while url == 0:
        dec = int(input('Enter only number 1/2/3> '))
        get_url(dec)

    print('Url =', url)

    stats = get_hook_info(url)
    print(stats)

    msg = "smth"
    while msg != "":
        print('\nEnter message, empty to end')
        msg = str(input("> "))
        if msg != "":
            send_message(url, msg)


if __name__ == '__main__':
    start()
