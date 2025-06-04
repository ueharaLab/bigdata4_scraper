# 口コミ全文を収集するクローラーを作る

[tabelog_scraper_reviewAll_test.py.py](/tabelog_scraper_reviewAll_test.py)にコードを追記して、口コミ一覧から本文全文を収集するプログラムを作成せよ。以下ヒント。
``` python

for pageNo in range(10):
    print('page=',pageNo+1)
    
    bodyRes = urllib.request.urlopen('https://tabelog.com/tokyo/A1304/A130402/13041176/dtlrvwlst/COND-0/smp1/?smp=1&lc=0&rvw_part=all&PG={}'.format(str(pageNo+1)))
    bodyHtml = bodyRes.read()

    root = lxml.html.fromstring(bodyHtml.decode('utf-8',errors='replace'))

    title_path = root.xpath("//a[@class='rvw-item__title-target']")
    for title in title_path:

        # 1.スライドp.37 のように.get(‘href’)で口コ全文ページへのリンクをスクレイピング

        # 2.スライドp.36 のようにhttps://tabelog.com/を連結して url.requestする

        # 3.本文全文を意味するタグを見つけ出す

        # 4.本文全文をスクレピング

```