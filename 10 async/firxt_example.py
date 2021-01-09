import asyncio
import time


async def tick():
    print("Tick")
    await asyncio.sleep(1)
    print("Tock")


async def main():
    await asyncio.gather(tick(), tick(), tick())
    # for _ in range(3):
    #     tick()


if __name__ == "__main__":
    asyncio.run(main())

# asyncio.get_event_loop() # возвращает работающий event loop или создает его
# loop.run_until_complete(fn)  # запускает event loop до завершения fn
# loop.close() закрытие event loop
# asyncio.run(fn())
# loop.create_task(fn())
# loop.run_forever() будет работать пока не будте вызван stop()
# loop.stop()