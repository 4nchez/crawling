from urllib.request import urlopen
import bs4
html_str = '''
<html>
<body>
<ul class="greet">
    <li>hello</li>
    <li>3333</li>
    <li>1111</li>
</ul>
<ul class="reply">
    <li>555</li>
    <li>qwqw3</li>
    <li>14558</li>
</ul>
</body>
</html>
'''
# url = "https://www.naver.com"
# html = urlopen(url)
bs_obj = bs4.BeautifulSoup(html_str, "html.parser")
# bs_obj = bs4.BeautifulSoup(html, "html.parser")
print(bs_obj.find_all("ul",{"class":"reply"}))
lis = bs_obj.find_all("li")
print(lis)
