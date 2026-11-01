# 시장별 집계: groupby
import pandas as pd

pd.set_option("display.unicode.east_asian_width", True)
pd.set_option("display.float_format", "{:,.0f}".format)   # 큰 수를 쉼표로, 소수점 없이
FILE = "../data/상장사_재무_2021_2025.xlsx"
df = pd.read_excel(FILE, sheet_name="2025")
info = pd.read_excel(FILE, sheet_name="회사정보")
df25 = df.merge(info[["종목코드", "시장", "업종"]], on="종목코드", how="left")
print(df25.groupby("시장")["매출액"].sum())
print(df25.groupby("시장")["매출액"].agg(["count", "sum", "median"]))
