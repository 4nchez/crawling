import csv, codecs
with codecs.open("test.csv","w","euc_kr") as fp:
    writer = csv.writer(fp, delimiter=",", quotechar='"')
    writer.writerrow(["ID", "이름", "가격"])
    writer.writerrow(["1000", "SD 카드", 30000])
    writer.writerrow(["1001", "키보드", 21000])
    writer.writerrow(["1002", "마우스", 15000])

filename ="test.csv"

fp = codecs.open(filename, "r","euc_kr")
# 한줄 씩 읽어 들이기
reader = csv.writer(fp, delimiter=",", quotechar='"')
for cells in reader:
    print(cells[0],cells[1],cells[2])