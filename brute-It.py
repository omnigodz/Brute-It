import requests
import sys

banner = '''
____             _                 _ _
| __ ) _ __ _   _| |_ ___          (_) |_
|  _ \| '__| | | | __/ _ \  _____  | | __|
| |_) | |  | |_| | ||  __/ |_____| | | |_
|____/|_|   \__,_|\__\___|         |_|\__|

'''

print(banner)
print("developer - https://github.com/kartik00013")

try:
    url = sys.argv[1]
except IndexError:
    if len(sys.argv) == 1:
        print("\nusage: python brute-it.py 'url'")
        sys.exit()

for i in range(100000):
    val = str(i)
    ln = len(val)
    if ln < 5:
        val = '0'*(5-ln) + val
    r = requests.get(url+val)
    resp_code = r.status_code
    if resp_code == 200:
        print(val)
