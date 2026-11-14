# 전년 대비 매출 성장률: 회사 · 연도 순서로 정렬한 뒤 groupby().pct_change()
import numpy as np
import pandas as pd

pd.set_option("display.unicode.east_asian_width", True)
FILE = "../data/상장사_재무_2021_2025.xlsx"
years = ["2021", "2022", "2023", "2024", "2025"]
books = pd.read_excel(FILE, sheet_name=years, dtype={"종목코드": str})
parts = []
for y in years:
    t = books[y].copy()
    t["연도"] = int(y)
    parts.append(t)
df = pd.concat(parts, ignore_index=True)

df = df.sort_values(["종목코드", "연도"])                       # 회사별로 연도 순서
df["매출성장률"] = df.groupby("종목코드")["매출액"].pct_change()  # (올해 / 전년) - 1
for name in ["삼성전자", "카카오"]:
    print(df[df["회사명"] == name][["연도", "회사명", "매출액", "매출성장률"]].round(4))

g25 = df[df["연도"] == 2025]["매출성장률"]
print(len(g25), g25.isna().sum(), np.isinf(g25).sum())
print(df[np.isinf(df["매출성장률"])][["연도", "회사명", "매출액"]].head(3))

# 전년 매출액이 0이면 inf: 빈칸으로 바꿈
df["매출성장률"] = df["매출성장률"].replace([np.inf, -np.inf], np.nan)
g25 = df[df["연도"] == 2025]["매출성장률"]
print(len(g25), g25.isna().sum(), np.isinf(g25).sum())
