# 새 열 계산 복습: 열끼리 계산하면 같은 행끼리 계산됨
import pandas as pd

pd.set_option("display.unicode.east_asian_width", True)
FILE = "../data/상장사_재무_2021_2025.xlsx"
df = pd.read_excel(FILE, sheet_name="2025", dtype={"종목코드": str})
info = pd.read_excel(FILE, sheet_name="회사정보", dtype={"종목코드": str})
df25 = df.merge(info[["종목코드", "시장", "업종"]], on="종목코드", how="left")
print(df25.shape)

names = ["삼성전자", "SK하이닉스", "현대자동차", "유한양행", "카카오뱅크"]
d = df25[df25["회사명"].isin(names)].copy()          # 다섯 회사만 고른 복사본
d["매출액_억"] = d["매출액"] / 100                    # 백만 원 -> 억 원
d["영업이익_억"] = d["영업이익"] / 100
d["영업비용_억"] = d["매출액_억"] - d["영업이익_억"]  # 매출액 가운데 영업에 든 비용
d["영업손실"] = d["영업이익"] < 0                     # True / False
print(d[["회사명", "매출액_억", "영업이익_억", "영업비용_억", "영업손실"]])
