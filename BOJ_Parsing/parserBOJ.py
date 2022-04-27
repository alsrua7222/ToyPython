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

    def processParsing(self, DEBUG=False):
        # url 옵션 = 채점 할 수가 없는 문제, 번외 문제 제외함. 문제번호 오름차순
        # 현재 최대 페이지 수는 150. - 22/4/27
        MAX_PAGE = 150
        
        collect = []
        for page in range(1, 3+1):
            url = f"https://www.acmicpc.net/problemset?sort=no_asc&solvedac_option=xz%2Cxn&style=off%2Ccs&style_if=nand&page={page}"
            res = self.getResource(url, True)
            
            if res.status_code // 100 != 2:
                raise Exception(f"{res.status_code} error")
            
            bs = BeautifulSoup(res.text, "html.parser")

            table_row = bs.find("div", {"class": "table-responsive"}).find("tbody").find_all("tr")
            for v in table_row:
                tmp = []
                id = v.find("td", {"class": "list_problem_id"}).text
                sub = v.find_all("a")
                    
                tmp.append(int(id))
                tmp.append(sub[0].text)
                tmp.append(int(sub[1].text))
                tmp.append(int(sub[2].text))
                tmp.append(float(sub[3].text))
                collect.append(tmp)
        return collect



if __name__ == "__main__":
    p = Parse()
    print(*p.processParsing(), sep="\n")