# 빈칸(결측값) 세기
import pandas as pd

pd.set_option("display.unicode.east_asian_width", True)
df = pd.read_excel("../data/상장사_재무_2021_2025.xlsx", sheet_name="2025")
print(df.isna().sum())
print(df[df["매출액"].isna()][["회사명", "영업이익", "당기순이익"]].head(5))
