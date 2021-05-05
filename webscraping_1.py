try:
    import requests
    import json
    from bs4 import BeautifulSoup
except ModuleNotFoundError as e:
    import sys

    print(e)
    input("Press to exit ..")
    sys.exit()


class WebScrapingOne:
    def __init__(self, url: str, page_number: int) -> None:
        self.page_number = page_number
        self.url = url
        self.file = open("memes.json", "a", encoding="UTF-8")
        self.get_image()

    def get_image(self):
        for number in range(1, self.page_number + 1):
            params = {
                "page": number
            }
            req = requests.get(self.url, params=params)
            content = req.text
            soup = BeautifulSoup(content, "lxml")
            images = soup.find_all("img", {"class": "base-img"})
            for image in images:
                # print(image.get("src"))
                image_json = {
                    "image->": image.get("src")
                }
                json_data = json.dumps(image_json, ensure_ascii=False)
                self.file.write(json_data + "\n")
            print(f"Done Page >>{number}")
        self.file.close()

        print("\n")
        print("Done Scraping")


if __name__ == "__main__":
    try:
        pageNumber = int(input("Enter The Page Number >>"))
        WebScrapingOne("https://imgflip.com/", page_number=pageNumber)
    except Exception as error:
        print(error)
