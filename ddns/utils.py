import re
from typing import Generator

import requests

from ddns.settings import Result

ipaddr = re.compile(r"\d{1,3}.\d{1,3}\.\d{1,3}\.\d{1,3}")


def get_public_ip(url: str, result: Result) -> str:
    if result.type == 'json':
        return requests.get(url).json()[result.key]
    return ipaddr.search(requests.get(url).text).group(int(result.key))


def get_public_ip_or_none(url: str, result: Result) -> str | None:
    try:
        return get_public_ip(url, result)
    except Exception:
        return None


def generate_url(url_pool: dict[str, Result]) -> Generator[tuple[str, Result], None, None]:
    while True:
        for url, result in url_pool.items():
            yield url, result
