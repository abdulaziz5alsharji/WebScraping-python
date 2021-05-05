try:
    from selenium import webdriver
    from time import sleep
except ModuleNotFoundError as e:
    import sys

    print(e)
    input("Press any key to exit ..")
    sys.exit()
browser = webdriver.Chrome()
browser.get("https://www.google.com")
browser.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[2]/div[1]/div[1]/div/div[2]/input").send_keys(
    "Programming")
browser.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[2]/div[1]/div[3]/center/input[1]").click()
sleep(2)
titles = browser.find_elements_by_tag_name("h3")
for title in titles:
    print(title.text)
