import os
import threading
import psutil
import requests
import random
from concurrent.futures import ThreadPoolExecutor

uuidList = list()

def generate_string():
    return dict(data=f"string{str(random.randint(123, 1000000))}")

def send_requests(data):
    response = requests.post('http://127.0.0.1:3000/new_collection', json=data, headers={'accept': 'application/json', 'Content-Type': 'application/json'})
    return response

count = 0
batch_size = 24  # Number of requests to send in each batch
executor = ThreadPoolExecutor(max_workers=psutil.cpu_count())

while count < 9846153:
    threads = []
    batch_data = []

    for _ in range(batch_size):
        batch_data.append(generate_string())

    for data in batch_data:
        current_thread = executor.submit(send_requests, data)
        threads.append(current_thread)

    for thread in threads:
        result = thread.result()

    count += len(threads)
    os.system("clear")
    print(count)

executor.shutdown()
