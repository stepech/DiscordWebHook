from reformator import reformator
import requests

DISCORD_WEBSITE = "https://discord.com/api/webhooks/"
URLS_FOLDER = "urls.txt"


def normalrun(urls):
    print("\nPick number of bot to be used")

    try:
        x = int(input("> "))
    except:
        print("Choose only valid number between 1 and", str(len(urls)))
        normalrun(urls)
        quit()

    i = 1
    for key in urls:
        if i == x:
            bot = urls[key]
            break
        i += 1
    r = requests
    info = r.get(DISCORD_WEBSITE + bot)
    info = info.text
    print(info)

    payload = {}
    print("Do you want to use default name (seen above) or use your own?")
    y = input("Leave empty for default name or enter your name > ")
    if y != "":
        payload["username"] = y

    print("Do you want to use default image or use your own?")
    y = input("Leave empty for default image or enter url to your own > ")
    if y != "":
        payload["avatar_url"] = y

    while True:
        print("\nEnter your message, empty to end")
        message = input("> ")
        if message == "":
            break

        message = reformator(message)
        payload["content"] = message

        r.post(DISCORD_WEBSITE + bot, json=payload)


def open_file(file):
    try:
        f = open(file, 'r')
    except:
        print('There is no file ' + file + ', do you want to create one? (Y/N)')
        response = str(input("> "))
        if response == "Y" or response == "y":
            f = open(file, 'x')
            f.close()
            f = open(file, 'r')
        else:
            quit()
    print("Opened", file)
    return f


def start():
    urlsfile = open_file(URLS_FOLDER)
    urls = {}
    for line in urlsfile:
        urls[line.rstrip()] = urlsfile.readline().rstrip()
    urlsfile.close()

    print("Loaded", len(urls), "bots...")
    i = 1

    for key in urls:
        print(i, "=", key)
        i += 1

    normalrun(urls)


if __name__ == '__main__':
    start()
