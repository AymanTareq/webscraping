import scraper_helper as sh
BOT_NAME = 'amazon'

SPIDER_MODULES = ['amazon.spiders']
NEWSPIDER_MODULE = 'amazon.spiders'

AUTOTHROTTLE_ENABLED = True
ROBOTSTXT_OBEY = False

DEFAULT_REQUEST_HEADERS = sh.get_dict(
"""
    accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
    accept-encoding: gzip, deflate, br
    accept-language: en-US,en;q=0.9,bn;q=0.8
    cache-control: no-cache
    cookie: session-id=139-1036895-0881462; session-id-time=2082787201l; i18n-prefs=USD; sp-cdn="L5Z9:BD"; ubid-main=134-3277045-7855553; x-amz-captcha-1=1610224000976620; x-amz-captcha-2=da4Z8nfJVfNsms0+Sxeyjw==; session-token=cIdtpCW6Bug1dyjr/nqHW/PoeKX0PU8w6pm7QY0Es6/EwCZznRzE1eQpv2Nvne/ebfyqMgIIVaF4DePikIqwMvsXt8tmpd9VP43OTKZa7B91WDbcvTpwx5oAb1CUAMN/BcHbIFRlGwUynJQ6DmXCjNNvt9ZtMaiwDV9c9lhsTOGaJJDWiktvOfK4WiEFl6SW; skin=noskin; lc-main=en_US; csm-hit=tb:1MW8SG8MSX8M7JHXNMST+s-07X9CEMSGJA714S6MRP7|1613354224286&t:1613354224286&adb:adblk_yes
    downlink: 1.45
    ect: 3g
    pragma: no-cache
    rtt: 400
    sec-fetch-dest: document
    sec-fetch-mode: navigate
    sec-fetch-site: same-origin
    sec-fetch-user: ?1
    upgrade-insecure-requests: 1
    user-agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36
"""
)





