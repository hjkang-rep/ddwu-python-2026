# 시트 전체를 한 번에 읽기: sheet_name=None 이면 {시트 이름: 표} 딕셔너리
import pandas as pd

books = pd.read_excel("../data/상장사_재무_2021_2025.xlsx", sheet_name=None)
for name, sheet in books.items():
    print(name, sheet.shape)

info = books["회사정보"]
print(info["고유번호"].head(3))
info2 = pd.read_excel("../data/상장사_재무_2021_2025.xlsx", sheet_name="회사정보", dtype={"고유번호": str})
print(info2["고유번호"].head(3))
