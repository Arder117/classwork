import scrapy

class WeatherSpider(scrapy.Spider):
    name = 'weather_spider'
    allowed_domains = ['weather.com.cn']
    start_urls = ['http://www.weather.com.cn/shandong/index.shtml']

    def parse(self, response):
        # 选择城市名称和天气预报内容
        cities = response.xpath('//div[@class="t"]/a/text()').extract()
        forecasts = response.xpath('//div[@class="t"]/span/text()').extract()

        # 处理数据
        weather_data = []
        for city, forecast in zip(cities, forecasts):
            weather_data.append(f"{city}: {forecast}")

        # 将数据写入文件
        with open('weather.txt', 'w', encoding='utf-8') as f:
            for data in weather_data:
                f.write(data + '\n')

        self.log('Weather data saved to weather.txt')
