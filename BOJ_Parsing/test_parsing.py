import requests, re

url = "https://www.acmicpc.net/problem/1021"
res = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
print(res.status_code)

# print(res.text)
# 문제 제목 구하기
regex1 = re.compile('<span id="problem_title">(.*)</span>')
# 시간 제한, 메모리 제한, 제출, 정답, 맞힌 사람, 정답 비율 파싱하기
regex2 = re.compile("<tr><td>(.*) 초 </td><td>(.*) MB</td><td>(.*)</td><td>(.*)</td><td>(.*)</td><td>(.*)%</td></tr>")
print(regex1.findall(res.text))
print(regex2.findall(res.text))