import requests
import bs4

end = "http://api.visitkorea.or.kr/openapi/service/rest/KorService/areaBasedList?"
ServiceKey = "bxSO1gDZPdO64oTmEugUY0bf5qvfMZ84%2F5%2BxENo5lr7QEiUW%2BiTysfoBSvJ%2BZM5%2BxAhJLh%2B%2BPzx0oxZkAKBiFQ%3D%3D"

numOfRows = "10"
pageSize = "1"
pageNo = "1"
MobileOS = "ETC"
MobileApp = "AppTest"
arrange = "A"
contentTypeId = "15"
areaCode = "1"
sigunguCode = "4"
listYN = "Y"
# http://api.visitkorea.or.kr/openapi/service/rest/KorService/areaBasedList?ServiceKey=인증키&contentTypeId=15&areaCode=4&sigunguCode=4&MobileOS=ETC&MobileApp=AppTest
paramset = "serviceKey=" + ServiceKey + "&numOfRows=" + numOfRows + "&pageSize=" +\
           pageSize + "&pageNo=" + pageNo + "&MobileOS=" + MobileOS + "&MobileApp=" + \
           MobileApp + "&arrange=" + arrange + "&contentTypeId=" + contentTypeId + \
           "&areaCode=" + areaCode + "&sigunguCode=" + sigunguCode + "&listYN=" + listYN + "&_type=json"

url = end + paramset
print(url)
result = requests.get(url)
bs_obj = bs4.BeautifulSoup(result.content, "html.parser")
print(bs_obj)
