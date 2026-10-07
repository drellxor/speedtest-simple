import sys
import time
import urllib.request

N = 10

url = sys.argv[1]
req = urllib.request.Request(url, headers={"User-Agent": "speedtest/1.0"})
total_bytes = 0
total_time = 0.0

for i in range(1, N + 1):
    start = time.perf_counter()
    with urllib.request.urlopen(req, timeout=60) as resp:
        size = len(resp.read())
    elapsed = time.perf_counter() - start
    total_bytes += size
    total_time += elapsed
    print(f"{i:2}: {size / 1e6:.2f} MB за {elapsed:.2f} с")

print(f"Среднее время запроса: {total_time / N:.2f} с")
print(f"Скачано всего: {total_bytes / 1e6:.2f} MB")
print(f"Скорость: {total_bytes / 1e6 / total_time:.2f} MB/s ({total_bytes * 8 / 1e6 / total_time:.2f} Mbit/s)")
