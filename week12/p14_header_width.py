# pandas로 저장한 뒤 openpyxl로 열어 열 너비와 머리글 서식 정하기
import pandas as pd
from openpyxl import load_workbook
from openpyxl.styles import Alignment, Font, PatternFill

FILE = "../data/상장사_재무_2021_2025.xlsx"
OUT = "../내작업/p14_머리글.xlsx"
df = pd.read_excel(FILE, sheet_name="2025", dtype={"종목코드": str})
info = pd.read_excel(FILE, sheet_name="회사정보", dtype={"종목코드": str})
df25 = df.merge(info[["종목코드", "시장", "업종"]], on="종목코드", how="left")
ph = df25[df25["업종"] == "의약품 제조업"].copy()
ph["매출액(억 원)"] = ph["매출액"] / 100
ph["영업이익(억 원)"] = ph["영업이익"] / 100
ph["영업이익률"] = ph["영업이익"] / ph["매출액"].where(ph["매출액"] > 0)
cols = ["회사명", "시장", "매출액(억 원)", "영업이익(억 원)", "영업이익률"]
table = ph.sort_values("매출액", ascending=False)[cols]
table.to_excel(OUT, sheet_name="회사별", index=False)       # 1. pandas로 값 저장

wb = load_workbook(OUT)                                       # 2. openpyxl로 열기
ws = wb["회사별"]
widths = {"A": 24, "B": 10, "C": 15, "D": 16, "E": 12}
for col, w in widths.items():
    ws.column_dimensions[col].width = w                       # 열 너비(글자 수 정도)

head_font = Font(bold=True, color="FFFFFF")                   # 굵게, 흰 글자
head_fill = PatternFill(fill_type="solid", fgColor="1F4E79")  # 진한 파랑 채움
for cell in ws[1]:                                            # 1행의 셀 전부
    cell.font = head_font
    cell.fill = head_fill
    cell.alignment = Alignment(horizontal="center")
wb.save(OUT)                                                  # 3. 다시 저장
print(ws.dimensions, ws["A1"].value, ws["A1"].font.b, ws["A1"].fill.fgColor.rgb)
print(ws.column_dimensions["A"].width, ws.column_dimensions["F"].width)
