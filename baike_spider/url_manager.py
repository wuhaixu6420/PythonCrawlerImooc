#url管理器

class UrlManager(object):
    def __init__(self):
        #创建两个set集合，存放 没有解析的url  和  已经解析过的url
        self.new_urls = set()
        self.old_urls = set()

    def add_new_url(self, url):
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)

    def add_new_urls(self, urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            #将url添加到未解析的utl集合中
            self.add_new_url(url)

    def has_new_url(self):
        #判断没有解析的url集合中是否存在数据
        return len(self.new_urls) != 0

    def get_new_url(self):
        #从没有解析的urk集合中提取出一条数据，并添加到解析过得url集合中
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url
