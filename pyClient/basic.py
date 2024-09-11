import requests

endpoint = "https://httpbin.org/anything"

get_response = requests.get(endpoint, json={"query":"This is just a simple test"})
print(get_response.json())


"""
txt:
-------
{
  "args": {}, 
  "data": "", 
  "files": {}, 
  "form": {}, 
  "headers": {
    "Accept": "*/*", 
    "Accept-Encoding": "gzip, deflate", 
    "Host": "httpbin.org", 
    "User-Agent": "python-requests/2.32.3", 
    "X-Amzn-Trace-Id": "Root=1-66e13f97-78f67d645720df8813b51948"
  }, 
  "json": null, 
  "method": "GET", 
  "origin": "103.106.236.97", 
  "url": "https://httpbin.org/anything"
}


json:
------
{'args': {}, 'data': '', 'files': {}, 'form': {}, 'headers': {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate', 'Host': 'httpbin.org', 'User-Agent': 'python-requests/2.32.3', 'X-Amzn-Trace-Id': 'Root=1-66e13faf-00b7f34d0ab3a2547d269a78'}, 'json': None, 'method': 'GET', 'origin': '103.106.236.97', 'url': 'https://httpbin.org/anything'}




"""