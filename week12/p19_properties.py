# 문서 속성: 작성자 · 마지막 수정자 · 제목
from openpyxl import load_workbook

wb = load_workbook("../내작업/p18_그림.xlsx")         # p18을 먼저 실행해 둠
p = wb.properties
print("바꾸기 전:", p.creator, "/", p.lastModifiedBy, "/", p.title)

p.creator = "Hojun Kang"                              # 자기 이름으로 바꿔 씀
p.lastModifiedBy = "Hojun Kang"
p.title = "의약품 제조업 보고서"
wb.save("../내작업/p19_속성.xlsx")

p2 = load_workbook("../내작업/p19_속성.xlsx").properties
print("바꾼 뒤:", p2.creator, "/", p2.lastModifiedBy, "/", p2.title)
