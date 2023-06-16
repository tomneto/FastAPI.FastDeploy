import threading
import psutil
import requests
import random


uuidList = list()

def createUser(username, password):
	data = dict(user=username, password=password)
	response = requests.post('https://python-vercel-sample-api.vercel.app/example', json=data, headers={'accept': 'application/json', 'Content-Type': 'application/json'})
	uuidList.append(response.json())
	return response

while True:
	threads = list()

	for e in range(psutil.cpu_count()):
		user = f"user{str(random.randint(123, 1000000))}"
		password = f"password{str(random.randint(123, 910000000))}"
		currentThread = threading.Thread(target=createUser, args=(user, password))
		currentThread.start()

		threads.append(currentThread)

	for e in threads:
		result = e.join()

	print(len(uuidList))
	print(uuidList)
