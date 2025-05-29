from urllib.request import urlopen
import urllib.request
import urllib.parse
import urllib
import lxml.html



for pageNo in range(10):
    print('page=',pageNo+1)
    
    bodyRes = urllib.request.urlopen('https://tabelog.com/tokyo/A1304/A130402/13041176/dtlrvwlst/COND-0/smp1/?smp=1&lc=0&rvw_part=all&PG={}'.format(pageNo+1))
    bodyHtml = bodyRes.read()
    root = lxml.html.fromstring(bodyHtml.decode('utf-8',errors='replace'))
    #rvw-item__title-target
    title_path = root.xpath("//a[@class='rvw-item__title-target']")

    for title in title_path:
        print(title.text_content())
        
'''
for pageNo in range(10):
    print('page=',pageNo+1)
    
    bodyRes = urllib.request.urlopen('https://tabelog.com/tokyo/A1304/A130402/13041176/dtlrvwlst/COND-0/smp1/?smp=1&lc=0&rvw_part=all&PG={}'.format(str(pageNo+1)))
    bodyHtml = bodyRes.read()
    body = bodyHtml.decode('utf-8')
    #print(body)
    titles=re.findall('(<a class="rvw-item__title-target" .*<strong>)([一-龥ぁ-んァ-ンー々]+)(</strong></a>)',body)
    for t in titles:
        print(t[1])
'''