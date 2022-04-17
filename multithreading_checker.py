from concurrent.futures import ThreadPoolExecutor
from typing import List, Tuple

import requests
from requests.exceptions import ConnectionError


def is_working_link(link: str) -> bool:
    try:
        r = requests.get(link)
    except ConnectionError:
        return False
    else:
        return True


def multithreading_check(links: List[str]) -> Tuple[int, int]:
    with ThreadPoolExecutor(max_workers=16) as executor:
        ok_count = sum(executor.map(is_working_link, links))
    broken_count = len(links) - ok_count

    return broken_count, ok_count
