# html下载器
import urllib.request as urllib2


class HtmlDownloader(object):

    def download(self, url):
        if url is None:
            return None
        #获取url中所显示的信息
        response = urllib2.urlopen(url)

        #200标识符代表正常获取
        if response.getcode() != 200:
            return None
        #读取url所显示的信息
        return response.read()
