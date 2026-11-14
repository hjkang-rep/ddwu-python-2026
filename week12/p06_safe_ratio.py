# 분모가 0 이하이면 지표를 빈칸(NaN)으로: where
import numpy as np
import pandas as pd

pd.set_option("display.unicode.east_asian_width", True)
FILE = "../data/상장사_재무_2021_2025.xlsx"
df25 = pd.read_excel(FILE, sheet_name="2025", dtype={"종목코드": str})

sales = df25["매출액"].where(df25["매출액"] > 0)        # 0 이하인 칸은 NaN
equity = df25["자본총계"].where(df25["자본총계"] > 0)
df25["영업이익률"] = df25["영업이익"] / sales
df25["순이익률"] = df25["당기순이익"] / sales
df25["부채비율"] = df25["부채총계"] / equity
df25["ROE"] = df25["당기순이익"] / equity

cols = ["영업이익률", "순이익률", "부채비율", "ROE"]
print(df25[cols].isna().sum())
print(np.isinf(df25[cols]).sum().sum())                # inf는 0개
print((df25[cols] * 100).describe().round(1))           # % 단위로 바꾼 뒤 요약
