import time

from loguru import logger

from ddns.ddns import huawei_ddns
from ddns.settings import settings
from ddns.utils import get_public_ip_or_none, generate_url


def main():
    url_pool = generate_url(settings.url_pool)
    current_ip = get_public_ip_or_none(*next(url_pool))
    while True:
        start = time.time()
        public_ip = get_public_ip_or_none(*next(url_pool))
        if public_ip is None:
            continue
        if public_ip != current_ip:
            huawei_ddns(ip=public_ip)
            current_ip = public_ip
        logger.info(f"Current IP: {current_ip}")
        time.sleep(settings.rate - (time.time() - start))


if __name__ == "__main__":
    main()
