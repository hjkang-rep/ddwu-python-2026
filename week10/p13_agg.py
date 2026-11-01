# 업종별 요약표: 이름을 붙인 agg
import pandas as pd

pd.set_option("display.unicode.east_asian_width", True)
FILE = "../data/상장사_재무_2021_2025.xlsx"
df = pd.read_excel(FILE, sheet_name="2025")
info = pd.read_excel(FILE, sheet_name="회사정보")
df25 = df.merge(info[["종목코드", "시장", "업종"]], on="종목코드", how="left")
s = (df25.groupby("업종")
         .agg(회사수=("회사명", "count"), 매출합계=("매출액", "sum"), 매출중앙값=("매출액", "median"))
         .sort_values("매출합계", ascending=False))
s["매출합계_조"] = (s["매출합계"] / 1_000_000).round(1)
print(s[["회사수", "매출합계_조", "매출중앙값"]].head(8))
