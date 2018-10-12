# coding=utf-8
import scrapy
from LagouMenu.items import LagoumenuItem
import faker
import random


class LaGouMenu(scrapy.Spider):
    name = 'lagoumenu'
    start_urls = ['https://www.lagou.com/']
    # 随机cookie, 随机ua
    init = faker.Faker(locale='zh_CN')
    lis = []
    for i in range(10):
        nn = init.user_agent()
        lis.append(nn)

    cookies = ['user_trace_token=20180703163453-d653a4fb-1474-403e-8478-9a30babd675e; _ga=GA1.2.1110294607.1530606829; LGUID=20180703163459-f9242c49-7e9b-11e8-bd8e-525400f775ce; JSESSIONID=ABAAABAAAGGABCBE627A8B73EFB7CD4544BD31E21BF7568; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1539325898; _gat=1; _gid=GA1.2.1147779459.1539325898; LGSID=20181012143120-6e6b7596-cde8-11e8-bbbf-5254005c3644; PRE_UTM=; PRE_HOST=; PRE_SITE=; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; index_location_city=%E5%85%A8%E5%9B%BD; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1539325967; LGRID=20181012143229-97a88fc7-cde8-11e8-b0cb-525400f775ce',
               '_ga=GA1.2.517327740.1537433691; user_trace_token=20180920165449-d4d71c20-bcb2-11e8-a275-525400f775ce; LGUID=20180920165449-d4d72096-bcb2-11e8-a275-525400f775ce; index_location_city=%E5%8C%97%E4%BA%AC; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=4; JSESSIONID=ABAAABAAAFCAAEG6C7E690F4F627F8CF6DC6EF282C33A52; X_HTTP_TOKEN=2ba16b3e1176657ba97bb2933e8ab57d; LGSID=20181012135907-ee9991ed-cde3-11e8-bbbf-5254005c3644; PRE_UTM=; PRE_HOST=; PRE_SITE=; PRE_LAND=; TG-TRACK-CODE=index_navigation; SEARCH_ID=9f5e28f6b5054eae90bba7e1a01adbdf; LG_LOGIN_USER_ID=d4e494df15974391e721bc7e19b18b37b83c438da1e7f46e; _putrc=71F16D06C60C5DD7; login=true; unick=%E4%BB%98; gate_login_token=f7166da628abe0698fb491d327bf18a1429794d682ad2408; _gat=1; LGRID=20181012142136-1283ff73-cde7-11e8-bbbf-5254005c3644']
    headers = {
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Connection': 'keep-alive',
        'Content-type': 'application/json;charset=utf-8',
        'Host': 'www.lagou.com',
        'Cookie': random.choice(cookies),
        'Referer': 'https://www.lagou.com/',
        'User-Agent': random.choice(lis)
    }

    def parse(self, response):
        menu_links = response.xpath('//*[@class="menu_box"]//dd/a/@href').extract()
        menu_texts = response.xpath('//*[@class="menu_box"]//dd/a/text()').extract()
        for link in menu_links:
            yield scrapy.Request(link, callback=self.parse_number, headers=self.headers)


    def parse_number(self, response):
        '''
        发起首页请求和后续页请求
        获取一共有多少后续,发起请求
        '''
        yield scrapy.Request(response.url, callback=self.parse_item, headers=self.headers)

        number_url = response.xpath('//*[@class="pager_container"]/a[last()-1]/text()').extract()[0]
        for number in range(2, int(number_url)+1):
            links = response.url + str(number) + '/'
            yield scrapy.Request(links, callback=self.parse_item, headers=self.headers)

    def parse_item(self, response):
        item = LagoumenuItem()
        print(response.url)
        positions = response.xpath('//*[@class="p_top"]/a/h3/text()').extract()
        moneys = response.xpath('//*[@class="money"]/text()').extract()
        experiences = response.xpath('//*[@class="p_bot"]/div/text()[3]').extract()
        company_names = response.xpath('//*[@class="company_name"]/a/text()').extract()
        for position, money, experience, company_name in zip(positions, moneys, experiences, company_names):
            item['position'] = position.strip()
            item['money'] = money
            item['experience'] = experience.strip()
            item['company_name'] = company_name
            yield item
