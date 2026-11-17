# 1단계: 영업이익률 열 만들기 (2025년, 금액 단위는 백만 원)
import pandas as pd

pd.set_option("display.unicode.east_asian_width", True)
pd.set_option("display.float_format", "{:,.1f}".format)   # 숫자를 쉼표 · 소수 한 자리로 보여 줌
FILE = "../data/상장사_재무_2021_2025.xlsx"
df = pd.read_excel(FILE, sheet_name="2025", dtype={"종목코드": str})

df["영업이익률"] = df["영업이익"] / df["매출액"] * 100   # 2,585행을 한 줄로 계산

cols = ["회사명", "매출액", "영업이익", "영업이익률"]
names = ["삼성전자", "SK하이닉스", "하이브"]
print(df[df["회사명"].isin(names)][cols].to_string(index=False))
