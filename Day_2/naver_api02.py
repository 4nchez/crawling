import os
import sys
import requests
from urllib.parse import urlparse
keyword = "광운대"
url = "https://openapi.naver.com/v1/search/blog?query=" + keyword # json 결과
result = requests.get(urlparse(url).geturl(), headers={"X-Naver-Client-Id":"Q92Fl0iqHMCMyN2hekCT", "X-Naver-Client-Secret":"3vcCxHfNO4"})
json_obj =result.json()
# for item in json_obj['items']:
#     print(item)
print(json_obj['lastBuildDate'])
print(json_obj['total'])
print(json_obj['start'])
print(json_obj['display'])