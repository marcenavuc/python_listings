import asyncio

import aiofiles


def read_large_file():
    with open("data/big_file.txt") as file:
        return file.read()

async def async_read_large_file():
    async with aiofiles.open("data/big_file.txt") as f:
        return await f.read()


def count_words(txt):
    return len(txt.split())


async def async_main():
    text = await async_read_large_file()
    print(count_words(text))


def main():
    text = read_large_file()
    print(count_words(text))


if __name__ == "__main__":
    # asyncio.run(async_main())
    async_main()
    main()
