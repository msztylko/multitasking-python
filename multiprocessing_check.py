from concurrent.futures import ProcessPoolExecutor

import requests
from requests.exceptions import ConnectionError


def is_working_link(link):
    try:
        r = requests.get(link)
    except ConnectionError:
        return False
    else:
        return True


def multiprocess_check_links(n, links):
    with ProcessPoolExecutor(max_workers=n) as executor:
        ok_count = sum(executor.map(is_working_link, links))
    broken_count = len(links) - ok_count

    return broken_count, ok_count
