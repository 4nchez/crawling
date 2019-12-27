import requests
from bs4 import BeautifulSoup

# url = "https://bp.eosgo.io/listing/eos-candy/"
url = "https://bp.eosgo.io/"
result = requests.get(url=url)
bs_obj = BeautifulSoup(result.content, "html.parser")


def get_bp_info(url):
    result = requests.get(url)
    bs_obj = BeautifulSoup(result.content, "html.parser")

    dname = bs_obj.find("div", {"class": "profile-name"})
    name = dname.find("h1")
    name = name.text

    ggps = bs_obj.find("div", {"class": "buttons medium button-plain"})
    gps = ggps.find("span")
    gps = gps.text

    al = bs_obj.find("div", {"class": "buttons medium button-outlined"})
    # print(al)
    if al is None:
        al = 'None'
    else:
        al = al.find("span")
        al = al.find("a")
        al = al['href']

    # 내용 끌기
    a=[]
    btext = bs_obj.find("div", {"class": "pf-body"})
    btext = btext.findAll("p")
    for b in btext:
        a.append(b.text)

    list = {}
    list['name']=name
    list['location']=gps
    list['link']=al
    list['content']=a
    return list

lf_items = bs_obj.findAll("div", {"class":"lf-item"})
hrefs = [div.find("a")["href"]for div in lf_items]
for number in range(0, 22):
    dic_res = get_bp_info(hrefs[number])
    print(dic_res)