import asyncio
from typing import List, Tuple

import aiohttp
from aiohttp import client_exceptions


async def check_link(session, link):
    try:
        async with session.get(link) as response:
            return response.status == 200
    except client_exceptions.ClientConnectionError as e:
        return False
    else:
        return True


async def asyncio_check(links: List[str]) -> Tuple[int, int]:
    async with aiohttp.ClientSession() as session:
        tasks = []
        for link in links:
            tasks.append(check_link(session, link))

        results = await asyncio.gather(*tasks)

    ok_count = sum(result for result in results)
    broken_count = len(links) - ok_count

    return broken_count, ok_count
