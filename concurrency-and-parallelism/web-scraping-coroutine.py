import time
import asyncio
import aiohttp
from aiohttp import ClientSession


async def fetcher(session: ClientSession, url: str) -> str:
    async with session.get(url) as response:
        return await response.text()


async def main():
    urls = ["https://www.naver.com", "https://facebook.com", "https://instagram.com"] * 10

    async with aiohttp.ClientSession() as session:
        result = await asyncio.gather(*[fetcher(session, url) for url in urls])  # url unpacking
        print(result)


if __name__ == "__main__":
    start = time.time()
    asyncio.run(main())
    end = time.time()
    print(f"time = {end - start}")
