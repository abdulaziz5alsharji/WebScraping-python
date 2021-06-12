import sys

try:
    import os
    import requests
    from platform import system
    from pyfiglet import figlet_format
    from termcolor import colored
    from bs4 import BeautifulSoup
    import re
except ModuleNotFoundError as error:
    print(colored(error, color="red"))
    input(colored("[!]Press Any Key To Exit .. ", color="red"))
    sys.exit()

clear = lambda: os.system("cls") if system() == "Windows" else os.system("clear")


def getCode():
    url = "https://influencer.redeemly.com/influencer/5f7b125e8539127b2e2c617c"
    content = requests.get(url=url).text
    code = re.compile(r'{"code":"(.*?)"},').findall(content)[0]
    return code


if __name__ == '__main__':
    clear()
    print(colored(figlet_format("Like Code"), color="blue"))
    input(colored("[+]Press To Start...", color="blue"))
    print("\n")
    print(colored(f"Code: {getCode()}", color="blue"))
