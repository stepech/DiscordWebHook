import requests


DISCORD_WEBSITE = "https://discord.com/api/webhooks/"

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
    urlsfile = open_file("urls.txt")
    urls = {}
    for line in urlsfile:
        urls[line.rstrip()] = urlsfile.readline().rstrip()

    print("Loading", len(urls), "bots...")


if __name__ == '__main__':
    start()
