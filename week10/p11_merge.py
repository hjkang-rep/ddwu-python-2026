# 연도 시트에 회사정보(시장 · 업종) 붙이기: merge
import pandas as pd

pd.set_option("display.unicode.east_asian_width", True)
FILE = "../data/상장사_재무_2021_2025.xlsx"
df = pd.read_excel(FILE, sheet_name="2025")
info = pd.read_excel(FILE, sheet_name="회사정보")
df25 = df.merge(info[["종목코드", "시장", "업종"]], on="종목코드", how="left")
print(df.shape, df25.shape)
print(df25[["회사명", "시장", "업종", "매출액"]].head())
print(df25["업종"].isna().sum())
