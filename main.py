from normal_mode import normal
from add_bot import add_bot

DISCORD_WEBSITE = "https://discord.com/api/webhooks/"
URLS_FOLDER = "urls.txt"


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

    if len(urls) == 0:
        add_bot()
    else:
        try:
            choice = int(input("Do you want to use one of loaded (1) or add new(2)"))
            if choice == 1:
                normal(urls)
            elif choice == 2:
                add_bot()
                start()
            else:
                print("Enter only '1' or '2'")
                quit()
        except:
            print("Enter only '1' or '2'")
            quit()


if __name__ == '__main__':
    start()
