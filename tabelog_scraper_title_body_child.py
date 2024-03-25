from urllib.request import urlopen
import urllib.request
import urllib.parse
import urllib
import lxml.html


def childTexts(node):
    title=''
    body=''
    for child in list(node):
        class_text = child.get('class')
        
        if class_text == "rvw-item__title rvw-item__title--rvwlst" :#１つ下の階層なので、これを指定
            
            title=child.text_content()
            
        elif class_text == "rvw-item__rvw-comment rvw-item__rvw-comment--custom" :
            
            body=child.text_content()
            
        
    return title, body 



f = open('tabelog_kuchikomi.html', 'r', encoding='UTF-8')
bodyHtml = f.read()

root = lxml.html.fromstring(bodyHtml)
#div class="rvw-item__visit-contents">
all_path = root.xpath("//div[@class='rvw-item__visit-contents']")

for i,text in enumerate(all_path):
    title, body=childTexts(text)
    print(title)
    
    print(body)
    if i >5:
        break
    
    

