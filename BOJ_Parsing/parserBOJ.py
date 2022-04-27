import requests
from bs4 import BeautifulSoup

class Parse:
    def __init__(self):
        return

    def getResource(self, url, User_Agent=False):
        if User_Agent:
            return requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
        else:
            return requests.get(url)

    def processParsing(self, DEBUG=False, MAX_PAGE=150):
        # url 옵션 = 채점 할 수가 없는 문제, 번외 문제 제외함. 문제번호 오름차순
        # 현재 최대 페이지 수는 150. - 22/4/27
        collect = []
        for page in range(1, MAX_PAGE+1):
            url = f"https://www.acmicpc.net/problemset?sort=no_asc&solvedac_option=xz%2Cxn&style=off%2Ccs&style_if=nand&page={page}"
            res = self.getResource(url, True)
            
            if res.status_code // 100 != 2:
                raise Exception(f"{res.status_code} error")
            
            bs = BeautifulSoup(res.text, "html.parser")

            table_row = bs.find("div", {"class": "table-responsive"}).find("tbody").find_all("tr")
            for tr in table_row:
                tmp = []
                td = tr.find_all("td")
                
                # id
                tmp.append(int(td[0].text))

                # title
                tmp.append(td[1].find("a").text)
                
                # solved
                tmp.append(int(td[3].find("a").text))

                # submit
                tmp.append(int(td[4].find("a").text))

                # ac_rate
                tmp.append(float(td[5].text[:-1]))
                collect.append(tmp)
        return collect



if __name__ == "__main__":
    p = Parse()
    print(*p.processParsing(DEBUG=False, MAX_PAGE=1), sep="\n")