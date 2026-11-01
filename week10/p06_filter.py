# 조건으로 행 고르기 (금액 단위: 백만 원)
import pandas as pd

pd.set_option("display.unicode.east_asian_width", True)
df = pd.read_excel("../data/상장사_재무_2021_2025.xlsx", sheet_name="2025")
big = df[df["매출액"] >= 10_000_000]          # 매출액 10조 원 이상
print(len(big))
loss = df[(df["매출액"] >= 1_000_000) & (df["영업이익"] < 0)]   # 매출 1조 원 이상인데 영업손실
print(len(loss))
print(loss[["회사명", "매출액", "영업이익"]].head())
