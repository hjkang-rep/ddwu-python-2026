# openpyxl의 통합 문서 · 시트 · 셀
from openpyxl import Workbook, load_workbook

wb = Workbook()                  # 새 통합 문서. 시트 하나가 들어 있음
ws = wb.active                   # 지금 선택된 시트
print(wb.sheetnames)
ws.title = "연습"                # 시트 이름 바꾸기

ws["A1"] = "회사명"              # 주소로 셀 하나에 쓰기
ws["B1"] = "매출액(억 원)"
ws.cell(row=2, column=1, value="유한양행")    # 행 번호 · 열 번호로 쓰기
ws.cell(row=2, column=2, value=21866)
ws.append(["대웅", 20684])       # 마지막 행 아래에 한 행 추가
wb.save("../내작업/p13_첫통합문서.xlsx")

wb2 = load_workbook("../내작업/p13_첫통합문서.xlsx")    # 저장한 파일을 다시 열기
ws2 = wb2["연습"]
print(wb2.sheetnames, ws2.max_row, ws2.max_column)
print(ws2["B2"].value, ws2.cell(row=3, column=1).value)
for row in ws2.iter_rows(values_only=True):   # 행마다 값만 꺼내기
    print(row)
