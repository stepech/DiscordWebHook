import requests
from secretsu import get_url
from secretsu import reformator

def get_hook_info(url):

    response = requests.get(url)
    return response.text


def send_message(url, msg):
    payload = {
        "username": "Oskar",
        "content": msg,
        "avatar_url": "https://i.imgur.com/Q5W52JU.png"
    }
    requests.post(url, json=payload)


def start():

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
            msg = reformator(msg)
            send_message(url, msg)


if __name__ == '__main__':
    start()
