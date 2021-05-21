# Scrapy settings for yelp_scraping project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'yelp_scraping'

SPIDER_MODULES = ['yelp_scraping.spiders']
NEWSPIDER_MODULE = 'yelp_scraping.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'yelp_scraping (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
import scraper_helper as sh
DEFAULT_REQUEST_HEADERS = sh.get_dict(
"""
accept: */*
accept-encoding: gzip, deflate, br
accept-language: en-US,en;q=0.9,bn;q=0.8
cache-control: no-cache
content-type: application/json
cookie: wdi=1|C0FCD7F0165919B8|0x1.7fd02df6b28d8p+30|e02cfab72c92e60b; hl=en_US; _ga=GA1.2.C0FCD7F0165919B8; _fbp=fb.1.1609829339895.1453220780; __qca=P0-307744109-1609829339253; __adroll_fpc=af24654db637c55cfdb1f2545bf476f0-1609829470543; __ar_v4=R6CCT276HZCSDMYF3I2QLV%3A20210104%3A1%7CWVH5XECXTBG6NLPUBP3IAF%3A20210104%3A1%7C7YX6SJQ4RZAMPB6LZ7CHFF%3A20210104%3A71%7CQB5JPFIKRZDSBOZSULG4YB%3A20210104%3A74%7CBHPKS4B4ONEJJMGH4QCJZR%3A20210104%3A74%7CMWSLDXLFLNGOLIYRSDGTEZ%3A20210104%3A1; qntcst=D; bse=f9b9ab7fa93e4265a28a6e5e5d3f68b6; _gid=GA1.2.638101050.1614101982; g_state={"i_p":1614707049812,"i_l":3}; sc=93cde070c9; recentlocations=East+Capitol+St+NE+%26+First+St+SE%2C+Washington%2C+DC+20004%3B%3BUnited+States%3B%3BNew+York%2C+NY%2C+United+States%3B%3B91+King+William+Rd%2C+Adelaide+South+Australia+5000%2C+Australia%3B%3B; location=%7B%22city%22%3A+%22Washington%22%2C+%22zip%22%3A+%2220004%22%2C+%22country%22%3A+%22US%22%2C+%22address2%22%3A+%22%22%2C+%22address3%22%3A+%22%22%2C+%22state%22%3A+%22DC%22%2C+%22address1%22%3A+%22East+Capitol+St+NE+%26+First+St+SE%22%2C+%22unformatted%22%3A+%22E+Capitol+St+And+First+St+NW%2C+Washington%2C+DC+20004%22%7D; xcj=1|aQtrw07D7suD8MqMW_bcpR_RkVxYmpIkoUgT7g81lOE
pragma: no-cache
referer: https://www.yelp.com/search?find_desc=Real%20Estate%20Companies&find_near=united-states-capitol-washington-3
sec-fetch-dest: empty
sec-fetch-mode: cors
sec-fetch-site: same-origin
user-agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36

"""
)

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'yelp_scraping.middlewares.YelpScrapingSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'yelp_scraping.middlewares.YelpScrapingDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'yelp_scraping.pipelines.YelpScrapingPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
