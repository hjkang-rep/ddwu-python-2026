# 업종으로 고르기: 회사정보 시트의 종목코드 목록과 isin
import pandas as pd

pd.set_option("display.unicode.east_asian_width", True)
FILE = "../data/상장사_재무_2021_2025.xlsx"
df = pd.read_excel(FILE, sheet_name="2025")
info = pd.read_excel(FILE, sheet_name="회사정보")
semi = info[info["업종"] == "반도체 제조업"]
print(len(semi))
semi_fin = df[df["종목코드"].isin(semi["종목코드"])]
print(semi_fin.sort_values("매출액", ascending=False)[["회사명", "매출액", "영업이익"]].head())
print(info[info["회사명"] == "삼성전자"][["회사명", "업종"]])
