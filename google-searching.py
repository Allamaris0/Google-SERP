import requests
from fake_useragent import UserAgent
from lxml import html

ua = UserAgent()

class GoogleSearchScraper:
    def __init__(self, domain='com', language='en-US,en;q=0.5', headers=None):
        self.url = f'https://www.google.{domain}/search?q='

        random_ua = ua.random
        print(random_ua)
        if not headers:
            if language != 'en-US,en;q=0.5':
                language = f"{language}, 'en-US,en;q=0.5'"
            self.headers = {
                'Accept': '*/*',
                'Accept-Language': language,
                'User-Agent': random_ua,
            }
        else:
            self.headers = headers

        self.results = {}
        self.urls = []
        self.titles = []
        self.tries = 5

    def get_multiple_result(self, query: str, k: int):
        self.results = {}
        self.urls = []
        self.titles = []

        try:
            query = query.replace(" ","+")
        except:
            pass

        tries = 0

        while len(self.results)==0 or tries < self.tries:
            # print(tries)
            r = requests.get(self.url + query, headers=self.headers)
            assert r.status_code == 200

            tree = html.fromstring(r.content)

            for i in range(1, k + 1):
                xpath_expression = f'//*[@id="rso"]/div[{i}]//a'
                element = tree.xpath(xpath_expression)
                if element:
                    for el in element:
                        href = el.get('href')
                        h3 = el.xpath('.//h3')
                        if href and h3:
                            title = h3[0].text_content().strip()
                            self.urls.append(href.strip())
                            self.titles.append(title)
                            self.results[i] = {'url': href.strip(), 'title': title}
                            break
            tries += 1
