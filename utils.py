# Python
import requests
import time

#Third-party
from settings import url, headers, cache


@cache.cached(timeout=60*60) # пусть живет 1 час
def get_info():
    start = time.perf_counter()
    response = requests.request("GET", url, headers=headers)
    print(
        f'завершено за {(time.perf_counter() - start):.2f} секунд'
    )
    return response.json()