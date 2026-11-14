# 숫자 표시 형식(천 단위 쉼표, 퍼센트)과 틀 고정
from openpyxl import load_workbook

OUT = "../내작업/p14_머리글.xlsx"            # p14를 먼저 실행해 둠
wb = load_workbook(OUT)
ws = wb["회사별"]

for row in range(2, ws.max_row + 1):          # 2행부터 마지막 행까지
    ws.cell(row=row, column=3).number_format = "#,##0"      # C열: 21,866
    ws.cell(row=row, column=4).number_format = "#,##0"      # D열: 1,044
    ws.cell(row=row, column=5).number_format = "0.0%"       # E열: 4.8%
ws.freeze_panes = "B2"                         # 1행과 A열을 고정
wb.save("../내작업/p15_숫자형식.xlsx")

for addr in ["C2", "D2", "E2"]:
    c = ws[addr]
    print(addr, c.value, c.number_format)      # 값은 그대로, 보이는 모양만 바뀜
print(ws.freeze_panes)
