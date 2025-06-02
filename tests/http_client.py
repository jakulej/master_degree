import httpx
import time

x = '



for n in range(100):
    start = time.perf_counter()
    request = httpx.get('https://example.com')
    end = time.perf_counter()
    print((end-start)*1000,"ms")
