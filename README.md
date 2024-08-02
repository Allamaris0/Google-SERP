# Google-SERP
Simple scrapper of results from Google Search. This is my side project, so I decided to make it public. However if you need more advanced google scrapper, try free trial of SERP Scraper from Oxylabs.

# Usage
`git clone https://github.com/Allamaris0/Google-SERP.git`

Default domain is 'com' and default language is English. 

```
search = GoogleSearchScraper(domain='pl', language='pl-PL,pl;q=0.5')
query = "darmowy kurs python"

search.get_multiple_result(query=query, k=5)

print("URLs:", search.urls)
print("Titles:", search.titles)
print("Results:", search.results)
```

You can also add your headers
```
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept-Language': 'pl'
}

search = GoogleSearchScraper(domain='pl', headers=headers)
```

I don't know why, sometimes results are empty. I set default tries to 5. If you want to change it:
```
search = GoogleSearchScraper(domain='pl', language='pl-PL,pl;q=0.5')
search.tries = 10
```




