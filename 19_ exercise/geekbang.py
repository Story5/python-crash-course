import requests

url = "https://time.geekbang.org/serv/v1/column/details"

payload = "{\"is_article\":1,\"ids\":[305,296,252,218,207,200,169,163,161,142]}"
headers = {
  'Content-Type': 'application/json',
}

response = requests.request("POST", url, headers=headers, data = payload)

print(response.text.encode('utf8'))
