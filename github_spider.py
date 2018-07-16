import scrapy
import re

non_decimal = re.compile(r'[^\d.]+')

class TopReposSpider(scrapy.Spider):
    name = 'toprepos'
    download_delay = 15 # 15s
    custom_settings = {
        'COOKIES_ENABLED': False,
        'CONCURRENT_REQUESTS': 1,
        'AUTOTHROTTLE_ENABLED': True,
        'USER_AGENT': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36"
    }
    proxy_prefix = "https://thingproxy.freeboard.io/fetch/"
    start_url = "https://github.com/search?p=%d&q=is:public+stars:20..8900+state:open&s=stars&type=Repositories"

    def start_requests(self):
        urls = [(self.proxy_prefix if x % 2 == 0 else "") + (self.start_url % (x + 1)) for x in range(100)]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for repo_item in response.css('.repo-list .repo-list-item'):
            yield {
                'title': repo_item.css('h3 a::text').extract_first().strip(),
                'url': repo_item.css('h3 a::attr(href)').extract_first().strip(),
                'language': "".join(repo_item.css('.d-table-cell ::text').extract()).strip(),
                'stars': int(1000 * float(non_decimal.sub("", "".join(repo_item.css('.text-right ::text').extract()).strip()))),
                'updated': repo_item.css('relative-time::attr(datetime)').extract_first().strip()
            }