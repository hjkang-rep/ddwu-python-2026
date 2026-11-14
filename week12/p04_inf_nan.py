# 2025년 시트에서 지표를 계산하면 생기는 NaN과 inf
import numpy as np
import pandas as pd

pd.set_option("display.unicode.east_asian_width", True)
FILE = "../data/상장사_재무_2021_2025.xlsx"
df = pd.read_excel(FILE, sheet_name="2025", dtype={"종목코드": str})
info = pd.read_excel(FILE, sheet_name="회사정보", dtype={"종목코드": str})
df25 = df.merge(info[["종목코드", "업종"]], on="종목코드", how="left")

df25["영업이익률"] = df25["영업이익"] / df25["매출액"]
df25["순이익률"] = df25["당기순이익"] / df25["매출액"]
df25["부채비율"] = df25["부채총계"] / df25["자본총계"]
df25["ROE"] = df25["당기순이익"] / df25["자본총계"]

cols = ["영업이익률", "순이익률", "부채비율", "ROE"]
check = pd.DataFrame({
    "NaN": df25[cols].isna().sum(),
    "inf": (df25[cols] == np.inf).sum(),
    "-inf": (df25[cols] == -np.inf).sum(),
    "음수": (df25[cols] < 0).sum(),
})
print(check)
print(df25["영업이익률"].mean())                     # -inf가 섞여 평균도 -inf

blank = df25[df25["매출액"].isna()]                   # 매출액 빈칸
print(len(blank))
print(blank["업종"].value_counts().head(4))
zero = df25[df25["매출액"] == 0]                      # 매출액 0
print(len(zero), zero["회사명"].str.contains("스팩").sum())
print(zero[["회사명", "매출액", "영업이익", "당기순이익", "영업이익률", "순이익률"]].head(4))
