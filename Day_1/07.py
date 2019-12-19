import urllib.request
import bs4

url = "https://news.naver.com"
html = urllib.request.urlopen(url)

bs_obj = bs4.BeautifulSoup(html, "html.parser")

menu = bs_obj.findAll("ul",{"class":"mlist2 no_bg"})
li = menu[-1].findAll("li")
for lis in li:
    strong = lis.find("strong")
    print(strong.text)
