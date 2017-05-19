#爬虫总调度程序
from baike_spider import html_downloader
from baike_spider import html_outputer
from baike_spider import html_parser
from baike_spider import url_manager


class SpiderMain(object):
    def __init__(self):
        #类初始化
        #url管理器
        self.urls = url_manager.UrlManager()
        #html下载器
        self.downloader = html_downloader.HtmlDownloader()
        #html解析器
        self.parser = html_parser.HtmlParser()
        #html输出器
        self.outputer = html_outputer.HtmlOutPuter()

    def craw(self, root_url):
        #次数调控
        count =1
        #将初始url添加到url管理器里面
        self.urls.add_new_url(root_url)
        #判断url管理器里面是否还有可解析的url
        while self.urls.has_new_url():
            try:
                #从url解析器里面获取一个url
                new_url = self.urls.get_new_url()
                print('craw %d : %s' %(count, new_url))
                #将该url所显示的html下载下来
                html_cont = self.downloader.download(new_url)
                #解析html页面，返回所需要的数据，以及html中的url链接
                new_urls, new_data = self.parser.parser(new_url, html_cont)
                #将html解析出来的额utl链接的集合添加到utl管理器中
                self.urls.add_new_urls(new_urls)
                #将html解析器中解析的所需要的数据添加到html输出器的输出集合中
                self.outputer.collect_data(new_data)

                #次数限制，防止死循环
                if count == 10:
                    break
                count = count + 1
            except:
                print('craw failed')

        #爬去结束之后，html输出器将数据输出到文件中
        self.outputer.output_html()
        pass


if __name__=="__main__":
    root_url = "http://baike.baidu.com/item/Python"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)