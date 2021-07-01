import sys

try:
    import os
    import requests
    from pyfiglet import figlet_format
    from platform import system
    from termcolor import colored
except ModuleNotFoundError as error:
    print(colored(error, color="red"))
    input(colored("[!]Press Any Key To Exit .. ", color="red"))
    sys.exit()

clear = lambda: os.system("cls") if system() == "Windows" else os.system("clear")


def removeBackgroundFromImage(image_name: str, output_name: str) -> None:
    try:
        url = "https://api.remove.bg/v1.0/removebg"
        file = {'image_file': open(image_name, "rb")}
        data = {"size": "auto"}
        headers = {"X-Api-Key": "jh3KJF3mCTdspdM2ahkitnjY"}
        response = requests.post(url=url, data=data, files=file, headers=headers)
        if response.status_code == 200:
            with open(output_name, "wb") as image:
                image.write(response.content)
            print(colored("[++]================== REMOVED ==================[++]", color="blue"))
        else:
            print(colored("[++]================== ERROR ==================[++]", color="red"))
    except Exception as er:
        print(colored(er, color="red"))
        sys.exit()


if __name__ == '__main__':
    try:
        clear()
        print()
        print(colored(figlet_format("Remove Bg From Image"), color="blue"))
        print("\n")
        imageName = input(colored("[++]Image Name: ", color="blue"))
        outputName = input(colored("[++]Output Name: ", color="blue"))
        print("\n")
        print(colored("[++]Wait....", color="blue"))
        print("\n")
        removeBackgroundFromImage(imageName, output_name=outputName)
    except Exception as err:
        print(colored(err, color="red"))
        sys.exit()
