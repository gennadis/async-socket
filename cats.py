from time import time
import requests


def get_file(url):
    response = requests.get(url, allow_redirects=True)
    return response


def write_file(response):
    filename = response.url.split("/")[-1]
    with open(filename, "wb") as file:
        file.write(response.content)


def main(count):
    t0 = time()
    url = "https://loremflickr.com/320/240"

    for _ in range(0, count + 1):
        response = get_file(url)
        write_file(response)

    print(time() - t0)


if __name__ == "__main__":
    main(10)
