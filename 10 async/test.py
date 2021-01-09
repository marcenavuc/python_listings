import asyncio
import collections
import time


async def atick():
    print("Tick")
    await asyncio.sleep(1)
    print("Tock")


def tick():
    print("Tick")
    time.sleep(1)
    print("Tock")


if __name__ == "__main__":
    # for i in range(3):
        # tick()
        # asyncio.run(atick())
    # asyncio.run(atick(), atick(), atick())
    # asyncio.gather(atick(), atick(), atick())
    # loop = asyncio.get_event_loop()
    # print(asyncio.get_running_loop()) # raise RuntimeError
    loop = asyncio.get_event_loop()
    try:
        for i in range(3):
            # loop.run_until_complete(atick())
            loop.create_task(atick())
        loop.run_in_executor()
    except Exception as e:
        print(e)
