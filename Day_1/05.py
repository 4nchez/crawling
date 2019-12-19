import bs4
html_str = '''
<html>
<body>
<ul class="ko">
    <li><a href="https://www.naver.com">naver</a></li>
</ul>
<ul class="sns">
    <li><a href="https://www.facebook.com">facebook</a></li>
</ul>
</body>
</html>
'''

bs_obj = bs4.BeautifulSoup(html_str, "html.parser")
atag = bs_obj.find_all("a")
print(atag[0]['href'])
import urllib.request
import bs4

url = "https://www.naver.com"
html = urllib.request.urlopen(url)

bs_obj = bs4.BeautifulSoup(html, "html.parser")

top_right = bs_obj.find("div", {"class":"area_links"})
first_a = top_right.find("a")
print(first_a['href'])