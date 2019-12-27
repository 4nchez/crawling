import requests
from urllib.parse import urlparse
from urllib.request import urlopen
# url="http://www.krei.re.kr:18181/chart/main_chart/index/kind/W/sdate/1972-01-01/edate/2019-12-23"


def get_api_result(from_1, to_2):
    url = "http://www.krei.re.kr:18181/chart/main_chart/index_grid/kind/W/sdate/"+from_1+"/edate/"+to_2+"/mode/1"
    result = requests.get(urlparse(url).geturl())
    return result.json()

def call_and_print(from_1, to_2):
    json_obj = get_api_result(from_1,to_2)
    for item in json_obj['data']:
        title = item['date']
        # op = item['op']
        # cl = item['cl']
        # se = item['se']
        # vo = item['vo']
        print(title + "@" + item['op'] + "@" + item['cl'] + "@" + item['se'] + "@" + item['vo'])
from_1 = "2019-01-01"
to_2 = "2019-12-23"
call_and_print(from_1,to_2)