import requests
from bs4 import BeautifulSoup
headers = {'User-Agent':'Mozilla/5.0'}
url = "http://jolse.com/category/toners-mists/1019/"

result = requests.get(url, headers=headers)
# bs_obj = BeautifulSoup(result.text)
bs_obj = BeautifulSoup(result.content, "html.parser")

# 이름찾기
# dname = bs_obj.find("p", {"class": "name"})
# dname = dname.find("span").text
# print(dname)

# 가격찾기
# price = bs_obj.find("ul")
# price1 = price.findAll("span")
# price1 = price1[1].text
# print(price)

ul = bs_obj.find("ul",{"class":"prdList grid4"})


boxes = ul.findAll("div",{"class":"box"})

# 이름찾기
# for box in boxes:
#     dname = box.find("p", {"class": "name"})
#     span = dname.find("span")
#     print(span.text)

# 전체 찾기
def get_prouduct_info(box):
    dname = box.find("p", {"class": "name"})
    spans_name = dname.findAll("span")
    ul = box.find("ul")
    spans_price = ul.findAll("span")
    alink = box.find("a")
    name = spans_name[0].text
    price = spans_price[1].text
    link = alink['href']
    # print(price)
    return {"name":name, "price":price, "link":link}

for box in boxes:
    product_info = get_prouduct_info(box)
    print(product_info)

