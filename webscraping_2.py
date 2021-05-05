try:
    from time import sleep
    from selenium import webdriver
except ModuleNotFoundError as e:
    import sys

    print(e)
    input("Press any key to exit >>")
    sys.exit()


def google_calculator():
    browser = webdriver.Chrome()
    browser.get("https://www.google.com")
    browser.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[2]/div[1]/div[1]/div/div[2]/input").send_keys(
        "2x5")
    browser.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[2]/div[1]/div[3]/center/input[1]").click()
    sleep(2)
    print(browser.find_element_by_xpath(
        "/html/body/div[8]/div[2]/div[9]/div[2]/div/div[2]/div[2]/div/div/div[1]/div/div/div[1]/div/div/div[1]/div["
        "2]/div[2]/div/div/span").text) 


if __name__ == "__main__":
    google_calculator()
