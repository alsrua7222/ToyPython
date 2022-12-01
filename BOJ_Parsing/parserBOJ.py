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

    def processDetailParsing(self, DEBUG=False, Problem_ids=[]):
        if Problem_ids == []:
            raise Exception("No problem id")
        
        """
        출력 매개변수 설정
        1. 문제 번호
        2. 시간 제한
        3. 메모리 제한
        4. 제출 횟수
        5. 정답
        6. 맞힌 사람
        7. 정답 비율
        8. 문제 내용
        9. 입력 내용
        10. 출력 내용
        11. 알고리즘 분류
        12. 
        """
    def processParsing(self, DEBUG=False, MAX_PAGE=150):
        # url 옵션 = 채점 할 수가 없는 문제, 번외 문제 제외함. 문제번호 오름차순
        # 현재 최대 페이지 수는 150. - 22/4/27

        """
        출력 매개변수 설정
        1. 문제 번호
        2. 문제 제목
        3. 맞은 사람 수
        4. 제출 횟수
        5. 정답률 (맞은 사람 수 / (맞은 사람 수 + 첫 번째 맞기 전까지 틀린 횟수))
        """
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