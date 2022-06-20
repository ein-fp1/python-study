import requests
from requests import Session
import time


def fetcher(session: Session, url: str) -> str:
    with session.get(url) as response:
        return response.text


def main():
    urls = ["https://www.naver.com", "https://facebook.com", "https://instagram.com"] * 10

    # session = requests.Session()
    # session.get(url)
    # session.close()

    with requests.Session() as session:
        result = [fetcher(session, url) for url in urls]
        print(result)


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(f"time = {end - start}")
