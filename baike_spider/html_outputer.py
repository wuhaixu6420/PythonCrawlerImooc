#html输出器

class HtmlOutPuter(object):
    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        #数据追加
        self.datas.append(data)

    def output_html(self):
        #打开文件，没有则创建，并赋予写入权限
        fout = open('output.html', 'w', encoding='utf-8')
        #已以下的形式，输出到文件中
        fout.write("<html>")
        fout.write("<body>")
        fout.write("<table>")

        # ascii
        for data in self.datas:
            fout.write("<tr>")
            fout.write("<td>%s</td>" % data['url'])
            fout.write("<td>%s</td>" % data['title'])
            fout.write("<td>%s</td>" % data['summary'])
            fout.write("</tr>")

        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")

        #文件输出结束，关闭程序
        fout.close()