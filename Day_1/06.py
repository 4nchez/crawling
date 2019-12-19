import urllib.request
import bs4

url = "https://www.naver.com"
html = urllib.request.urlopen(url)

bs_obj = bs4.BeautifulSoup(html, "html.parser")

top_right = bs_obj.find("div", {"class":"area_links"})
first_a = top_right.find("a")
print(first_a['href'])
menu = bs_obj.findAll("ul",{"class":"an_l"})
li = menu[0].findAll("li")
for lis in li:
    strong = lis.find("span",{"class":"an_txt"})
    print(strong.text)
