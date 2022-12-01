# solved.ac 비공식 api
# https://solvedac.github.io/unofficial-documentation/#/operations/getProblemByIdArray

import http.client

conn = http.client.HTTPSConnection("solved.ac")

headers = { 'Content-Type': "application/json" }

conn.request("GET", "/api/v3/problem/show?problemId=1000", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))