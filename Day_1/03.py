from urllib.request import urlopen
import bs4
html_str = '''
<html>
<body>
<ul>
    <li>hello</li>
    <li>3333</li>
    <li>1111</li>
</ul>
</body>
</html>
'''
# url = "https://www.naver.com"
# html = urlopen(url)
# bs_obj = bs4.BeautifulSoup(html, "html.parser")
bs_obj = bs4.BeautifulSoup(html_str, "html.parser")
print(bs_obj.find("ul"))
li = bs_obj.find("li")
lis = bs_obj.find_all("li")
print(lis)
print(lis[2])
