import requests
import json

url = "https://api.newscatcherapi.com/v2/search?q=Apple&from=2023/2/15&to=1 day ago&countries=CA&page_size=1"

headers = {
    'x-api-key': 'f5TdwS1_7UMWFeIsOeyz5J2oKZxyI7C6fPQf-XFY6hY'
}
response = requests.request("GET", url, headers = headers, data = {})
#print(response.text)
j = json.dumps(response.json(), indent=4)
print(j)

# res=response.json()
# j = json.dumps(res, indent=4)
# print(j["page"])

l = json.loads(j)

print(type(l))
#j1=json.dumps(l)
#print(j1)
