try:
    import requests
    import re
    from bs4 import BeautifulSoup
except ModuleNotFoundError as error:
    import sys

    print(error)
    input("Press any key to exit ..")
    sys.exit()


class GetEmailAndPhoneNumber:
    def __init__(self):
        self.urls = [
            "https://elzero.org/category/challenges/",
            "https://elzero.org/"

        ]
        self.emails = []
        self.phoneNumber = []
        self.get_email()
        self.get_phone_number()

    def get_email(self):
        try:
            for url in self.urls:
                req_1 = requests.get(url)
                content = req_1.text
                soup = BeautifulSoup(content, "lxml")
                emails_ = soup.find_all("a", {"href": re.compile(r"^mailto:")})
                for email in emails_:
                    self.emails.append(email.get("href"))
        except requests.exceptions.ConnectionError:
            pass
        except Exception as e:
            print(e)
        print(self.emails)

    def get_phone_number(self):
        try:
            for url in self.urls:
                req_2 = requests.get(url)
                content_2 = req_2.text
                soup = BeautifulSoup(content_2, "lxml")
                phones = soup.find_all("a", {"href": re.compile(r"^tels:")})
                for phone in phones:
                    self.phoneNumber.append(phone.get("href"))
        except requests.exceptions.ConnectionError:
            pass
        except Exception as e:
            print(e)
        print(self.phoneNumber)


if __name__ == "__main__":
    GetEmailAndPhoneNumber()
