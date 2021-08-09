import sys

try:
    import csv
    import requests
    from bs4 import BeautifulSoup
except ModuleNotFoundError as error:
    print(error)
    input("Press Any Key To Exit..")
    sys.exit()


def Scraping() -> None:
    images = []
    titles = []
    prices = []
    url = "https://deals.souq.com/eg-en/smart-tvs/c/15236"
    content = requests.get(url).content
    soup = BeautifulSoup(content, "lxml")
    boxes = soup.findAll("div", {"class": "column-block"})
    for box in boxes:
        image = box.find("img")["data-src"]
        title = box.find("h6").text.strip()
        price = box.find("span", {"class": "is block sk-clr1"}).text.strip()
        images.append(image)
        titles.append(title)
        prices.append(price)

    with open(r"C:\Users\Dell\Desktop\test.csv", "a", encoding="UTF-8") as file:
        writer = csv.writer(file)
        writer.writerow(["image", "title", "price"])
        for index_ in range(len(images)):
            writer.writerow([images[index_], titles[index_], prices[index_]])
    print("DONE")


if __name__ == '__main__':
    Scraping()
