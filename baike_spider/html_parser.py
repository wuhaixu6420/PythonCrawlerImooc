#html解析器
from bs4 import BeautifulSoup
import re
from urllib.parse import urljoin


class HtmlParser(object):

    def _get_new_urls(self, page_url, soup):
        #创建set集合
        new_urls = set()
        #根据正则表达式，来获取html中的匹配链接      获取的都是相对路径
        links = soup.find_all('a', href=re.compile(r"/item/\S+"))
        for link in links:
            #获取相对路径
            new_url = link['href']
            #根据page_url的局对路径  将相对路径的new_url转化为绝对路径
            new_full_url = urljoin(page_url, new_url)
            #将转化好的绝对路径存放至set集合中
            new_urls.add(new_full_url)
        return new_urls

    def _get_new_data(self, page_url, soup):
        #创建字典型数据，类似java中map    已键值对存在 {key1:value1; key2:value2} "；"区别
        res_data = {}
        #将url链接存放到数据中
        res_data['url'] = page_url

        #解析html页面，将title存放到数据中
        title_node = soup.find('dd', class_="lemmaWgt-lemmaTitle-title").find("h1")
        res_data['title'] = title_node.get_text()

        #解析html页面，将summary存放到数据中
        summary_node = soup.find('div', class_="lemma-summary")
        res_data['summary'] = summary_node.get_text()

        return res_data


    def parser(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return
        #将url所显示的数据 html，已utf-8的编码形式，读取到本地
        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        #获取html中的url链接
        new_urls = self._get_new_urls(page_url, soup)
        #解析html页面，将所需要的数据解析出来
        new_dara = self._get_new_data(page_url, soup)
        return new_urls, new_dara
