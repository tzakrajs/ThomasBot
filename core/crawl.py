import aiohttp
import asyncio
import async_timeout

from core import main_loop

async def fetch(session, url):
    with async_timeout.timeout(10):
        async with session.get(url) as response:
            return await response.text()

async def main(loop):
    async with aiohttp.ClientSession(loop=main_loop) as session:
        html = await fetch(session, 'http://python.org')
        print(html)
