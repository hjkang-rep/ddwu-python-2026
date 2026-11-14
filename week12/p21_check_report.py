# 만든 보고서를 다시 읽어 확인: 시트 크기 · 합계 · 서식 · 그림 · 문서 속성
import pandas as pd
from openpyxl import load_workbook

pd.set_option("display.unicode.east_asian_width", True)
INDUSTRY = "의약품 제조업"
FILE = "../data/상장사_재무_2021_2025.xlsx"
OUT = f"../내작업/업종보고서_{INDUSTRY}.xlsx"         # p20을 먼저 실행해 둠

rep = pd.read_excel(OUT, sheet_name=None)              # 보고서의 모든 시트
for name, t in rep.items():
    print(name, t.shape)

# 원래 자료에서 다시 계산한 값과 맞춰 봄
df = pd.read_excel(FILE, sheet_name="2025", dtype={"종목코드": str})
info = pd.read_excel(FILE, sheet_name="회사정보", dtype={"종목코드": str})
src = df.merge(info[["종목코드", "업종"]], on="종목코드")
src = src[src["업종"] == INDUSTRY]
firms = rep["회사별"]
print(len(firms), len(src))
print(round(firms["매출액(억 원)"].sum()), round(src["매출액"].sum() / 100))
print(firms["회사명"].head(3).tolist())

wb = load_workbook(OUT)
ws = wb["회사별"]
red = sum(1 for row in ws.iter_rows(min_row=2) for c in row
          if c.font.color is not None and c.font.color.rgb == "00C00000")
print("빨간 칸", red, "| E2 형식", ws["E2"].number_format, "| H2 형식", ws["H2"].number_format)
print("그림", len(wb["연도별 추이"]._images), "| 작성자", wb.properties.creator,
      "| 마지막 수정자", wb.properties.lastModifiedBy)
