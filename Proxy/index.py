from http_request_randomizer.requests.proxy.requestProxy import RequestProxy
from fake_headers import Headers
import requests
import time
from multiprocessing import Pool
from selenium import webdriver

class RANDOM_PROXY:
    def __init__(self, n):
        self.proxy = self.proxy_create()
        # self.get()
        # self.post(n)
        self.createSelenium()
        # print(self.vote("programming", "2011150", "U", self.proxy.get_address()))
        # print(self.vote("programming", "2011150", "U"))
    def proxy_create(self):
        self.req_proxy = RequestProxy()
        proxy = self.test_proxy()  # 잘 작동되는 프록시 선별
        # print(3)
        return proxy

    def test_proxy(self):
        """
        가져온 프록시중에서 실제로 작동되는 프록시만 하나씩 가져오는 코드
        test_url : 자신의 IP를 확인하는 코드. 여기서 변경된 IP가 나오면 성공적으로 우회가된것
        """
        test_url = 'http://ipv4.icanhazip.com'
        while True:  # 제대로된 프록시가 나올때까지 무한반복
            request = self.req_proxy.generate_proxied_request(test_url)
            # print(1)
            if request is not None:
                print("\t Response: ip={0}".format(u''.join(request.text).encode('utf-8')))
                proxy = self.req_proxy.current_proxy
                break

            else:
                continue
        # print("Good")
        return proxy  # 잘작동된 proxy를 뽑아준다.


    def get(self):
        header = Headers(
            browser="chrome", # 크롬 버전
            os="win",  # 윈도우 버전
            headers=True  # 헤더 패킷 존재
        )

        # 랜덤 유저 에이전트를 생성해주는 함수.
        self.headers = header.generate()
        _url = "https://gall.dcinside.com/board/lists?id=programming"

        self.proxies = {}  # request.get 인자에 넣어줄 딕셔너리 생성
        self.proxies['http'] = 'http://%s' % self.proxy

        # html = requests.session().get(_url, headers=self.headers, proxies=self.proxies).content
        html = requests.get(_url, headers=self.headers, proxies=self.proxies)
        print(html.headers)
        print(html.content)
        # TODO:: html로 받아내서 하고 싶은 것 하기. or 따로 post를 처리해서 하고 싶은 것 하기.

    def post(self, n):
        header = Headers(
            browser="chrome",  # 크롬 버전
            os="win",  # 윈도우 버전프로그램
            headers=True  # 헤더 패킷 존재
        )
        self.headers = header.generate()
        self.headers["Origin"] = r"https://gall.dcinside.com"
        self.headers["Referer"] = r"https://gall.dcinside.com/board/view/?id=programming&no=2005618&page=1"

        url = r"https://gall.dcinside.com/board/recommend/vote"
        self.proxies = {}  # request.get 인자에 넣어줄 딕셔너리 생성
        self.proxies['http'] = 'http://%s' % self.proxy

        res = requests.post(url, headers=self.headers, proxies=self.proxies)
        print(self.headers)
        print(res.status_code)
        print(res.encoding)
        print(res.text)
        print(res.headers)
        print(res.request)
        return n

    def createSelenium(self):
        # print(self.proxy, type(self.proxy))
        proxy = self.proxy.get_address()
        # # print(self.proxy)
        # proxy = "211.237.5.73:8898"
        webdriver.DesiredCapabilities.CHROME['proxy'] = {
            'httpProxy': proxy,
            'ftpProxy': proxy,
            'sslProxy': proxy,
            'proxyType': "MANUAL"
        }
        url = "http://www.example.com/"
        # url = "https://gall.dcinside.com/board/lists/?id=programming"
        driver = webdriver.Chrome("../module/chromedriver.exe")
        driver.get(url)
        try:
            while True:
                pass
        except KeyboardInterrupt:
            pass
        return

    def vote(self, gall_id: str, no: str, mode: str, proxy: str = '') -> str:
        result = ''
        s = requests.session()
        s.headers.update({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'})
        if proxy:
            s.proxies = {'http': 'http://' + proxy}
        # r1 = s.get('http://gall.dcinside.com/board/view/?id=' + gall_id, timeout=5)
        r1 = s.get('http://gall.dcinside.com/board/view/?id=' + gall_id + '&no=' + no)
        s.headers.update({
            'Host': 'gall.dcinside.com',
            'Origin': 'http://gall.dcinside.com',
            'Referer': 'http://gall.dcinside.com/board/view/?id=' + gall_id + '&no=' + no,
            'X-Requested-With': 'XMLHttpRequest'
        })
        data = {
            'ci_t': s.cookies['ci_c'],
            'id': gall_id,
            'no': no,
            'mode': mode,
            'code_recommend': 'undefined',
            '_GALLTYPE_': 'G',
            'link_id': gall_id,
        }
        if mode == 'U':
            s.cookies.update({gall_id + no + '_Firstcheck': 'Y'})
        else:
            s.cookies.update({gall_id + no + '_Firstcheck_down': 'Y'})
        r2 = s.post('http://gall.dcinside.com/board/recommend/vote', data=data, timeout=5)
        result = r2.content.decode('utf-8').replace(
            '<script>window.location="https://gall.dcinside.com/board/recommend/vote"</script>', ''""'')
        if len(result) > 64:
            return 'err'
        # print(result)
        return result
if __name__ == "__main__":
    # p = Pool()
    # thread = p.map_async(RANDOM_PROXY, [i for i in range(1, 11)])
    # file = open(r"C:\Users\KMK\Downloads\post.txt", "w")
    # for v in thread.get():
    #     pass
    RANDOM_PROXY(1)

