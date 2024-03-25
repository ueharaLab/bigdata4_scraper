from urllib.request import urlopen
import urllib.request
import urllib.parse
import urllib
import lxml.html




f = open('tabelog_kuchikomi.html', 'r', encoding='UTF-8')
bodyHtml = f.read()

root = lxml.html.fromstring(bodyHtml)

body_path = root.xpath("//div[@class='rvw-item__rvw-comment rvw-item__rvw-comment--custom']")
title_path = root.xpath("//a[@class='rvw-item__title-target']")
for title,body in zip(title_path,body_path):
    print(title.text_content())
    print(body.text_content())

