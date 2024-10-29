# 安装Python扩展库scrapy，然后编写爬⾍项⽬，从⽹站 http://www.weather.com.cn/shandong/index.shtml 爬取⼭东各城市的天⽓预报数据，
# 并把爬取到的天⽓数据新建写⼊本地⽂本⽂件 weather.txt。

import scrapy
import re

class WeatherSpider(scrapy.Spider):
    name = 'weather'
    start_urls = ['http://www.weather.com.cn/shandong/index.shtml']

    def parse(self, response):
        for city in response.css('div.conMidtab2'):
            city_name = city.css('tr:nth-child(1) > td > a::text').get()
            city_weather = city.css('tr:nth-child(2) > td::text').get()
            city_temperature = city.css('tr:nth-child(3) > td::text').get()
            city_wind = city.css('tr:nth-child(4) > td::text').get()
            city_data = city_name + ' ' + city_weather + ' ' + city_temperature + ' ' + city_wind
            with open('weather.txt', 'a', encoding='utf-8') as f:
                f.write(city_data + '\n')
            yield {
                'city': city_name,
                'weather': city_weather,
                'temperature': city_temperature,
                'wind': city_wind
            }















