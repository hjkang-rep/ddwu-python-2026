# 연도 시트 다섯 개를 긴 표 하나로: pd.concat과 연도 열
import pandas as pd

pd.set_option("display.unicode.east_asian_width", True)
FILE = "../data/상장사_재무_2021_2025.xlsx"
years = ["2021", "2022", "2023", "2024", "2025"]
books = pd.read_excel(FILE, sheet_name=years, dtype={"종목코드": str})

parts = []
for y in years:
    t = books[y].copy()
    t["연도"] = int(y)                  # 어느 해의 행인지 적어 둠
    parts.append(t)
df = pd.concat(parts, ignore_index=True)  # 위아래로 이어 붙임
print(df.shape)
print(df["연도"].value_counts().sort_index())
print(df["종목코드"].dtype, df["종목코드"].nunique())
print(df[df["회사명"] == "동화약품"][["연도", "종목코드", "회사명", "매출액"]])

n = df.groupby("종목코드")["연도"].count()   # 회사마다 몇 해가 있는지
print(n.value_counts().sort_index())
