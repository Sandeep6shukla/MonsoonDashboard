import requests
import re

URL="https://dm.mcgm.gov.in/main.b3fa1c45a28b2635.js"

print("="*50)
print("MCGM JS INSPECTOR")
print("="*50)

r=requests.get(URL)

print()
print("Status :",r.status_code)

text=r.text

patterns=[

    r'https://[^"\']+',

    r'http://[^"\']+',

    r'/api/[^"\']+',

    r'/v1/[^"\']+',

    r'[A-Za-z0-9/_-]+\.json'

]

found=set()

for pattern in patterns:

    for match in re.findall(
        pattern,
        text
    ):

        found.add(match)

print()

print(
    "Potential Endpoints"
)

print("="*50)

for item in sorted(found):

    print(item)