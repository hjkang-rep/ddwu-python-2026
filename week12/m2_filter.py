# 2단계: 나눗셈이 이상하게 나온 행을 보고, 거르기
import pandas as pd

pd.set_option("display.unicode.east_asian_width", True)
pd.set_option("display.float_format", "{:,.1f}".format)   # 숫자를 쉼표 · 소수 한 자리로 보여 줌
FILE = "../data/상장사_재무_2021_2025.xlsx"
df = pd.read_excel(FILE, sheet_name="2025", dtype={"종목코드": str})
df["영업이익률"] = df["영업이익"] / df["매출액"] * 100
cols = ["회사명", "매출액", "영업이익", "영업이익률"]

# 거르기 전: 영업이익률이 큰 순서로 세우면 맨 위는?
print(df.sort_values("영업이익률", ascending=False)[cols].head(3).to_string(index=False))

# 매출액이 0인 회사의 영업이익률
print(df[df["매출액"] == 0][cols].head(3).to_string(index=False))
print("매출액 0:", (df["매출액"] == 0).sum(), "곳, 영업이익률 빈칸:", df["영업이익률"].isna().sum(), "곳")

# 거르기: 매출액이 0보다 크고, 영업이익이 빈칸이 아닌 회사만 남김
ok = df[(df["매출액"] > 0) & df["영업이익"].notna()]
print(len(df), "->", len(ok))
