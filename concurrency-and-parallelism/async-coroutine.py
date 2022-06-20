import asyncio
import time


async def delivery(name: str, mealtime: int) -> int:
    print(f"{name}에게 배달 완료!")
    await asyncio.sleep(mealtime)
    print(f"{name} 식사 완료, {mealtime}시간 소요...")
    print(f"{name} 그릇 수거 완료")
    return mealtime


async def main():
    # 동시 실행
    result = await asyncio.gather(
        delivery("A", 10),
        delivery("B", 3),
        delivery("C", 4),
    )
    print(result)


async def task():
    # 태스크 예약
    task1 = asyncio.create_task(delivery("A", 10))
    task2 = asyncio.create_task(delivery("B", 3))

    await task1
    await task2

if __name__ == "__main__":

    start = time.time()
    asyncio.run(main())  # coroutine 실행
    end = time.time()
    print(end - start)

    asyncio.run(task())
