# Sycronous Request will take 38 secound
"""
import requests

URL = "https://httpbin.org/uuid"

def fetch(session,url):
    with session.get(url) as response:
        print(response.json()["uuid"])

def main():
    with requests.Session() as session:
        for _ in range(100):
            fetch(session, URL)
            
main()

"""

# Multiprocessing Pool
"""
from multiprocessing.pool import Pool
from multiprocessing import Process, Queue, freeze_support

import requests

URL = 'https://httpbin.org/uuid'


def fetch(session, url):
    with session.get(url) as response:
        print(response.json()['uuid'])


def main():
    with Pool() as pool:
        with requests.Session() as session:
            pool.starmap(fetch,[(session,URL) for _ in range(100)])


if __name__ == '__main__':
    freeze_support()
    main()
    
"""

# ThreadPoolExecutor
# Sycronous Request will take 38 secound
"""
from concurrent.futures import ThreadPoolExecutor
from multiprocessing.connection import wait

import requests

URL = "https://httpbin.org/uuid"

def fetch(session,url):
    with session.get(url) as response:
        print(response.json()["uuid"])

def main():
    with ThreadPoolExecutor(max_workers=10) as excutor:
        with requests.Session() as session:
            excutor.map(fetch, [session] * 100 , [URL] * 100)
            excutor.shutdown(wait=True)
            

main()
"""


import asyncio

import aiohttp

from timerr import timer

URL = 'https://httpbin.org/uuid'


async def fetch(session, url):
    async with session.get(url) as response:
        json_response = await response.json()
        print(json_response['uuid'])


async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, URL) for _ in range(2)]
        await asyncio.gather(*tasks)



@timer(1, 1)
def func():
    # asyncio.run(main()) # This Request not working
    asyncio.get_event_loop().run_until_complete(main())