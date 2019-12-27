import openpyxl

# 엑셀파일 열기
filename = "stats_104102.xlsx"
book = openpyxl.load_workbook(filename)

# 맨 앞의 시트 추출하기
# sheet = book.worksheets[0]
#
# # 시트의 각 행을 순서대로 추출하기
# data = []
# for row in sheet.rows:
# 	data.append([row[0].value, row[9].value])
#
# # 필요없는 줄(헤더, 연도, 계) 제거하기
# del data[0]
# del data[1]
# del data[2]
#
# # 데이터를 인구 순서로 정렬합니다.
# data = sorted(data, key=lambda x:x[1])
#
# # 하위 5위를 출력합니다.
# for i, a in enumerate(data):
# 	if (i >= 5): break
# 	print(i+1, a[0], int(a[1]))
# 활성화된 시트 추출하기
sheet = book.active

for i in range(0 , 9):
    total = int(sheet[str(chr(i + 66)) + "3"].value)
    seoul = int(sheet[str(chr(i + 66)) + "4"].value)
    output = total - seoul
    print("서울 제외 인구 =", output)
    # 쓰기
    sheet[str(chr(i + 66)) + "21"]=output
    cell = sheet[str(chr(i + 66)) + "21"]
    # 폰트와 색상 변경해보기
    cell.font = openpyxl.styles.Font(size=14, color="FF0000")
    cell.number_format = cell.number_format

# 엑셀 파일 저장하기
filename = "population.xlsx"
book.save(filename)
print("OK")