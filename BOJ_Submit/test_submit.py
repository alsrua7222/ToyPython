"""
현재 사용 불가능.
BOJ가 reCAPTCHA를 사용하여, 자동 로그인을 할 수 없도록 되어 있음.

1. 유저 정보를 넣어도 안됨.
2. 텀 시간을 늘리고, 패턴을 불규칙하게 바꿔도 안됨.

해결 하는 방법
1. 로그인 인증 토큰을 빌릴 수 있도록 따로 연락 취해야 함.
2. 프로그램 구동 과정에 웹 브라우저를 핸들러로 잡고 유저가 직접 로그인 하도록 함.
"""

import requests
import json
from bs4 import BeautifulSoup

url = "https://www.acmicpc.net/"
sses = requests.session()
user_data = {}
with open("data.json", "r") as f:
    user_data = json.load(f)
print(user_data)

res = sses.post(url + "signin", data=user_data, headers={"User-Agent": "Mozilla/5.0"})
if res.status_code == 200:
    print(res.text)
else:
    print(f"{res.status_code} Error")
