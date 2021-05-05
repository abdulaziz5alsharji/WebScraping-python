try:
    import requests
    from bs4 import BeautifulSoup
    import threading
except ModuleNotFoundError as error:
    import sys

    print(error)
    input("Press any key to exit ..")
    sys.exit()


class GitHubEmails:
    def __init__(self, page_number):
        self.page_number = page_number
        self.thread()

    def get_email(self):
        for number in range(1, self.page_number + 1):
            req = requests.get(f"https://github.com/search?q=ionic&type=Users&p={number}")
            content = req.text
            soup = BeautifulSoup(content, "lxml")
            for email in soup.find_all("a", {"class": "Link--muted"}):
                print(email.text)

    def thread(self):
        threading.Thread(target=self.get_email).start()


if __name__ == "__main__":
    pageNumber = int(input("Enter the page number >>"))
    GitHubEmails(page_number=pageNumber)
