from marvelchampionspider.items import MarvelChampionsImage
import datetime
import scrapy

class MarvelSpider(scrapy.Spider):
    name = "marvel-spider"
    start_urls = ["http://www.cardgamedb.com/index.php/marvelchampions/marvel_champions/_/core-set/?sort_col=field_795&sort_order=asc&per_page=1000"]

    def parse(self, response):
        filename = 'cardlist.txt'
        images = response.xpath('//img[@class="OtherImage"]/@src').extract()
        names = response.xpath('//img[@class="OtherImage"]/@alt').extract()
        with open(filename, 'w') as f:
            for (image, name) in zip(images, names):
                f.write("cardname: " + name +"\n")
                f.write("image: " + image + "\n")

        for (image, name) in zip(images, names):
            yield MarvelChampionsImage(title=name, image_urls=[image])