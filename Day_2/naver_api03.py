import requests
from urllib.parse import urlparse

keyword = '광운대학교'
url = "https://openapi.naver.com/v1/search/blog?query="+keyword
result = requests.get(urlparse(url).geturl(),
         headers={"X-Naver-Client-Id":"Q92Fl0iqHMCMyN2hekCT",
                  "X-Naver-Client-Secret":"3vcCxHfNO4"})
# print(result.json())
json_obj = result.json()
# for item in json_obj['items']:
#     print(item)
# print(json_obj['title']),print(json_obj['link']) #당연히 안됨
# for item in json_obj['items']:
    # print('Title :'+item['title'],' Link :'+item['link'])
    # print('Title :'+item['title'].replace("<b>","").replace("<b>",""),' Link :'+item['link'])
print("display : " + str(json_obj['display']))
print("start : " + str(json_obj['start']))
print("items : " + str(json_obj['items']))