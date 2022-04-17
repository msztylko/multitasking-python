import asyncio
import random
import re
import time

import requests
from bs4 import BeautifulSoup

from asyncio_checker import asyncio_check
from multiprocessing_checker import multiprocessing_check
from multithreading_checker import multithreading_check
from sequential_checker import sequential_check


def get_links_from_wiki(fraction):
    wiki_url = "https://en.wikipedia.org/wiki/List_of_Nobel_laureates_in_Chemistry"
    r = requests.get(wiki_url)
    soup = BeautifulSoup(r.text, "html.parser")
    table = soup.table
    links = []

    for link in table.find_all("a"):
        links.append(link.get("href"))

    pattern = re.compile("\/wiki\/\w+$")
    good_links = [link for link in links if pattern.match(link)]
    base_url = "https://en.wikipedia.org/"
    full_links = [base_url + link for link in good_links]
    full_links = random.sample(full_links, round(fraction * len(full_links)))

    return full_links


def prepare_test_links(links):
    to_break = random.sample(links, round(0.1 * len(links)))
    broken = [link.replace("kipedia", "asdf") for link in to_break]
    broken_count = len(broken)
    ok_count = len(links)
    test_links = links + broken
    random.shuffle(test_links)
    return test_links, broken_count, ok_count


def benchmark():
    for frac in [0.25, 0.5, 0.75, 1.0]:
        full_links = get_links_from_wiki(frac)
        test_links, test_broken_count, test_ok_count = prepare_test_links(full_links)
        # benchmark
        print(f"\n *** Execution time for checking {len(test_links)} links *** \n")
        for fn in [
            sequential_check,
            multithreading_check,
            multiprocessing_check,
        ]:
            start = time.time()
            broken_count, ok_count = fn(test_links)
            end = time.time()

            assert broken_count == test_broken_count
            assert ok_count == test_ok_count
            print(f"Running {fn.__name__} \ttook {end - start:.2f} seconds")


async def async_benchmark():
    print("\n ****** AsyncIO benchmark ******\n")
    for frac in [0.25, 0.5, 0.75, 1.0]:
        full_links = get_links_from_wiki(frac)
        test_links, test_broken_count, test_ok_count = prepare_test_links(full_links)
        # benchmark
        print(f"\n *** Execution time for checking {len(test_links)} links *** \n")
        # AsyncIO
        start = time.time()
        broken_count, ok_count = await asyncio_check(test_links)
        end = time.time()

        assert broken_count == test_broken_count
        assert ok_count == test_ok_count
        print(f"Running asyncion_check took {end - start:.2f} seconds")


if __name__ == "__main__":
    benchmark()
    asyncio.run(async_benchmark())
