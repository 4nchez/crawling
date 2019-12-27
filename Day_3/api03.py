from urllib.parse import quote
import requests
import bs4

# end = "http://apis.data.go.kr/B552657/ErmctInsttInfoInqireService/getParmacyFullDown?"
end = "http://apis.data.go.kr/B552657/ErmctInsttInfoInqireService/getParmacyListInfoInqire?"
key = "bxSO1gDZPdO64oTmEugUY0bf5qvfMZ84%2F5%2BxENo5lr7QEiUW%2BiTysfoBSvJ%2BZM5%2BxAhJLh%2B%2BPzx0oxZkAKBiFQ%3D%3D"

Q0 = quote("서울특별시")
ORD = "NAME"
pageNo = "1"
startPage = "1"
numOfRows = "5000"
# pageSize = "10"

param = "serviceKey=" + key + "&Q0=" + Q0 + "&Q1="  +  \
        "&ORD" + ORD + "&pageNo=" + pageNo + "&startPage=" + startPage + \
        "&numOfRows=" + numOfRows

url = end + param
print("url : " + url)
result = requests.get(url)
bs_obj = bs4.BeautifulSoup(result.content, "html.parser")
items = bs_obj.findAll("item")
#
# for item in items:
#     tagged_item = item.find("dutyname")
#     print(tagged_item)
a=[]
count = 0
for item in items:
    tagged_item = item.find("dutytime1c")
    tagged_item2 = item.find("dutyname")
    if(tagged_item != None):
        close_time = int(tagged_item.text)
        if(close_time > 2100):
            a.append(tagged_item2.text)
            count += 1
print("서울특별시 내 월요일 9시 이후까지 하는 약국의 수 : " +str(count))
print("서울특별시 내 월요일 9시 이후까지 하는 약국의 이름"
      ""
      " : " +str(a))