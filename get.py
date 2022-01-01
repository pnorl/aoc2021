
import requests
import sys
year = 2021
cookie = open("cookie.txt").read()

if len(sys.argv) < 2:
    print('Usage: Provide the day as a parameter')
    sys.exit()

day = sys.argv[1]
url = "https://adventofcode.com/{}/day/{}/input".format(year, day)
cookies = {'session': cookie}
response = requests.get(url, cookies = cookies)

if (response.status_code != 200):
    print("Download failed with code {}".format(response.status_code))
    sys.exit()

sys.stdout.write(str(response.text.rstrip()))