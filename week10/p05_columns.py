# 열 꺼내기와 요약
import pandas as pd

pd.set_option("display.unicode.east_asian_width", True)
df = pd.read_excel("../data/상장사_재무_2021_2025.xlsx", sheet_name="2025")
sales = df["매출액"]                 # 열 하나: Series
print(type(sales).__name__, sales.shape)
print(df[["회사명", "매출액"]].head(3))   # 열 여러 개: DataFrame
print(df["매출액"].describe())
