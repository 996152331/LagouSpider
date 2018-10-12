# coding=utf-8
from fake_useragent import UserAgent


class RandomUserAgentMiddlware():
    def __init__(self, crawler):
        super(RandomUserAgentMiddlware, self).__init__()
        self.ua = UserAgent
        self.ua_type = crawler.setting.get("RANDOM_UA_TYPE", "random")

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler)

    def process_request(self, request, spider):
        def get_ua():
            return getattr(self.ua, self.ua_type)

        print(get_ua())
        request.headers.setdefault('User-Agent', get_ua())