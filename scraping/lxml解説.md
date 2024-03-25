# LXMLによるスクレイピング
デモで動かしたコード[tabelog_scraper_title.py](/tabelog_scraper_title.py)の解説
```  python
import urllib.request
import lxml.html

# htmlをツリー構造に変換したデータを生成
root = lxml.html.fromstring(html)

# ツリー構造データから目的のタグを検索（戻り値は、該当するタグデータのリスト）
title_path = root.xpath("//a[@class='rvw-item__title-target']")

#.xpath : lxmlのメソッド。引数に以下の規則に従うタグを指定すると該当のタグデータをリストとして戻す（オブジェクト型と呼ばれるデータに隠蔽される）
#　//　:ルート(<html>)
#   a　 :ルートの下にある任意の a タグ
#   a[@属性名='属性値’] : <a>のうち　属性名=属性値であるようなもの
for title in title_path:
    print(title.text_content())
# 検索したタグに囲まれた文字列を取り出す
.text_content()

```