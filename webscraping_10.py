import sys

try:
    import os
    import time
    from urllib.request import urlretrieve
    from selenium import webdriver
    from platform import system
    from termcolor import colored
    from pyfiglet import figlet_format
except ModuleNotFoundError as error:
    print(colored(error, color="red"))
    input(colored("[!!]Press Any Key To Exit..", color="red"))
    sys.exit()

clear = lambda: os.system("cls") if system() == "Windows" else os.system("clear")


class ImageDownloader:
    def __init__(self, driver):
        self.browser = driver

    def download(self, keyword: str, path: str) -> None:
        counter = 1
        self.browser.get("https://www.google.com/")
        time.sleep(2)
        self.browser.find_element_by_xpath(
            "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input").send_keys(keyword)
        self.browser.find_element_by_xpath(
            "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]").click()
        time.sleep(3)
        self.browser.find_element_by_xpath("/html/body/div[7]/div/div[3]/div/div[1]/div/div[1]/div/div[2]/a").click()
        time.sleep(3)
        images = self.browser.find_elements_by_tag_name("img")
        if not os.path.exists(f"{path}"):
            os.mkdir(path)
        print(colored(f"[++]START DOWNLOADING....", color="blue"))
        for image in images:
            url = image.get_attribute("src")
            if url is not None:
                urlretrieve(url, rf"{path}\{keyword}{counter}.png")
                counter += 1
        print("\n")
        print(colored(f"[++]DONE DOWNLOAD {counter} IMAGE", color="blue"))


if __name__ == '__main__':
    clear()
    print()
    print(colored(figlet_format("Image Downloader"), color="blue"))
    print("\n")
    KEYWORD = input(colored("[++]Keyword: ", color="blue"))
    PATH = input(colored("[++]Path: ", color="blue"))
    print("\n")
    browser = webdriver.Chrome()
    downloader = ImageDownloader(browser)
    downloader.download(KEYWORD, PATH)
