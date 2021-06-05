import requests
from bs4 import BeautifulSoup
import json
from termcolor import colored
imagesUrl = []
titles = []
prices = []

data = {

}


def getPageScours(page_number: int) -> None:
    productNumber = 0
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/87.0.4280.88 Safari/537.36"
    }
    for page in range(1, page_number + 1):
        print(colored(f"[+]START PAGE: {page}", color="red"))
        response = requests.get(
            f"https://www.sultan-center.com/fresh-foods/dairy-cheese-and-eggs/cheese-cream.html?p={page}",
            headers=headers)
        pageContent = response.content
        soup = BeautifulSoup(pageContent, "lxml")
        images = soup.findAll("img", {"class": "product-image-photo"})
        title = soup.findAll("a", {"class": "product-item-link"})
        price = soup.findAll("span", {"class": "price"})
        for index_ in range(len(images)):
            productNumber += 1
            print(colored(f"[+]Product {productNumber}", color="red"))
            print(colored(f'[Image] {images[index_]["src"].strip()}', color="blue"))
            print(colored(f'[Title] {title[index_].text.strip()}', color="blue"))
            print(colored(f'[Price] {price[index_].text.strip()}', color="blue"))
            imagesUrl.append(images[index_]["src"].strip())
            titles.append(title[index_].text.strip())
            prices.append(price[index_].text.strip())
            data[f"Product_{productNumber}"] = {
                "product_title": title[index_].text.strip(),
                "price": price[index_].text.strip(),
                "image": images[index_]["src"].strip()
            }


def addData(json_name: str) -> None:
    with open(json_name, "w") as jsonFile:
        jsonFile.write(json.dumps(data))


if __name__ == '__main__':
    getPageScours(3)
    addData(r"C:\Users\Dell\Desktop\test.json")
