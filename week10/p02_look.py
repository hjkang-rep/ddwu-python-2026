# 앞부분 · 자료형 보기
import pandas as pd

pd.set_option("display.unicode.east_asian_width", True)  # 한글이 섞인 표의 열 맞춤
df = pd.read_excel("../data/상장사_재무_2021_2025.xlsx", sheet_name="2025")
print(df[["종목코드", "회사명", "재무제표", "매출액", "영업이익"]].head())
print(df.dtypes)
