import copy

import requests
from requests import Session
import time
import os
import threading
from concurrent.futures import ThreadPoolExecutor


class FetcherParam:

    def __init__(self, session: Session, url: str):
        self.__session: Session = session
        self.__url: str = url

    @property
    def session(self):
        return self.__session

    @property
    def url(self):
        return self.__url


def fetcher(fetcher_param: FetcherParam) -> str:
    session = fetcher_param.session
    url = fetcher_param.url
    print(f"{os.getpid()} process | {threading.get_ident()} url: {url}")
    with session.get(url) as response:
        return response.text


def main():
    urls = ["https://www.naver.com", "https://facebook.com", "https://instagram.com"] * 10

    executor = ThreadPoolExecutor(max_workers=2)
    with requests.Session() as session:
        # result = [fetcher(session, url) for url in urls]
        # print(result)
        fetcher_params = [FetcherParam(session, url) for url in urls]
        results = list(executor.map(fetcher, fetcher_params))
        print(results)


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(f"time = {end - start}")
