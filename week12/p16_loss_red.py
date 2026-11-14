# 조건에 따른 글자색: 영업손실(음수)인 칸을 빨간 글자로
from openpyxl import load_workbook
from openpyxl.styles import Font

wb = load_workbook("../내작업/p15_숫자형식.xlsx")   # p15를 먼저 실행해 둠
ws = wb["회사별"]
red = Font(color="C00000")                           # 빨강

count = 0
loss = []
for row in range(2, ws.max_row + 1):
    for col in [4, 5]:                                # D열 영업이익, E열 영업이익률
        cell = ws.cell(row=row, column=col)
        if cell.value is not None and cell.value < 0:  # 빈칸(None)은 건너뜀
            cell.font = red
            count += 1
            if col == 4:
                loss.append(ws.cell(row=row, column=1).value)
wb.save("../내작업/p16_손실빨강.xlsx")
print("빨간 칸", count, "손실 회사", len(loss))
print(loss[:4])
