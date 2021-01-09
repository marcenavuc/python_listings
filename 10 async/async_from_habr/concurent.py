from collections import namedtuple
import time
import asyncio
from concurrent.futures import FIRST_COMPLETED
import aiohttp
from aiohttp import ClientSession

Service = namedtuple('Service', ('name', 'url', 'ip_attr'))

SERVICES = (
    Service('ipify', 'https://api.ipify.org?format=json', 'ip'),
    Service('ip-api', 'http://ip-api.com/json', 'query'),
    Service('borken', 'http://no-way-this-is-going-to-work.com/json', 'ip')
)


async def fetch_ip(service, session: ClientSession):
    start = time.time()
    print('Fetching IP from {}'.format(service.name))

    # response = await aiohttp.request('GET', service.url)
    response = await session.get(service.url)
    json_response = await response.json()
    ip = json_response[service.ip_attr]

    response.close()
    return '{} finished with result: {}, took: {:.2f} seconds'.format(
        service.name, ip, time.time() - start)


async def asynchronous():
    async with aiohttp.ClientSession() as session:
        futures = [fetch_ip(service, session) for service in SERVICES]
        # done, _ = await asyncio.wait(futures, return_when=FIRST_COMPLETED)
        done, _ = await asyncio.wait(futures)

    # print(done.pop().result())
    for future in done:
        try:
            print(future.result())
        except:
            print("Eroroor")

    # for future in pending:
    #     future.cancel()


ioloop = asyncio.get_event_loop()
ioloop.run_until_complete(asynchronous())
ioloop.close()
# asyncio.run(asynchronous())
