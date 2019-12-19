from urllib.request import urlopen
import bs4
html_str = '<html><div>hello</div><div>test</div><div>est</div></html>'
# url = "https://www.naver.com"
# html = urlopen(url)
bs_obj = bs4.BeautifulSoup(html_str, "html.parser")
# bs_obj = bs4.BeautifulSoup(html, "html.parser")

print(bs_obj)
print(bs_obj.find("div"))
print(bs_obj.find("div").text)
