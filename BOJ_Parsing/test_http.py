

# import http.client

# conn = http.client.HTTPConnection("localhost", port=8000)

# for i in range(1000):
#     conn.request("GET", "/")
#     res = conn.getresponse()
#     body = res.read()
#     print(res.status)

# conn.close()

import requests

with requests.Session() as sess:
    for i in range(1000):
        res = sess.get("http://localhost:8000")
        print(res.status_code)