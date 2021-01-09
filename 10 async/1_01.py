import asyncio
import time


async def tick():
    print("Tick")
    await asyncio.sleep(1)
    print("Tock")


async def main():
    awaitable_obj = asyncio.gather(tick(), tick(), tick())
    for task in asyncio.all_tasks():
        print(task)
    await awaitable_obj


if __name__ == "__main__":
    # asyncio.run(main())
    # coroutine = main()
    # print(coroutine)
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
        print("courutiones have finished")
    finally:
        loop.close()
        print("Loop", loop.is_closed())
