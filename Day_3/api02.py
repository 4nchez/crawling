from urllib.parse import quote
import requests
import bs4

# end = "http://apis.data.go.kr/B552657/ErmctInsttInfoInqireService/getParmacyFullDown?"
end = "http://apis.data.go.kr/B552657/ErmctInsttInfoInqireService/getParmacyListInfoInqire?"
key = "bxSO1gDZPdO64oTmEugUY0bf5qvfMZ84%2F5%2BxENo5lr7QEiUW%2BiTysfoBSvJ%2BZM5%2BxAhJLh%2B%2BPzx0oxZkAKBiFQ%3D%3D"

Q0 = quote("서울특별시")
Q1 = quote("강남구")
QT = "1"
QN = quote("백화점약국")
ORD = "NAME"
pageNo = "1"
startPage = "1"
numOfRows = "10"
pageSize = "10"

param = "serviceKey=" + key + "&Q0=" + Q0 + "&Q1=" + Q1 + "&QT=" + QT + "&QN=" + QN + \
        "&ORD=" + ORD + "&pageNo=" + pageNo + "&startPage=" + startPage + \
        "&numOfRows=" + numOfRows + "&pageSize=" + pageSize

url = end + param
print("url : " + url)
result = requests.get(url)
bs_obj = bs4.BeautifulSoup(result.content, "html.parser")
items = bs_obj.findAll("item")

for item in items:
    tagged_item = item.find("dutyname")
    print(tagged_item)