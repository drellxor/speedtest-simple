import http.client
import sys
import time
import urllib.request

N = 10

url = sys.argv[1]
req = urllib.request.Request(url, headers={"User-Agent": "speedtest/1.0"})
total_bytes = 0
total_time = 0.0
ok = 0

for i in range(1, N + 1):
    start = time.perf_counter()
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            size = len(resp.read())
    except (OSError, http.client.HTTPException) as e:
        print(f"{i:2}: ошибка: {e}")
        continue
    elapsed = time.perf_counter() - start
    ok += 1
    total_bytes += size
    total_time += elapsed
    print(f"{i:2}: {size / 1e6:.2f} MB за {elapsed:.2f} с")

if not ok:
    sys.exit("Все запросы завершились ошибкой")

print(f"Успешных запросов: {ok} из {N}")
print(f"Среднее время запроса: {total_time / ok:.2f} с")
print(f"Скачано всего: {total_bytes / 1e6:.2f} MB")
print(f"Скорость: {total_bytes / 1e6 / total_time:.2f} MB/s ({total_bytes * 8 / 1e6 / total_time:.2f} Mbit/s)")
