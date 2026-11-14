# 자본총계가 음수인 회사(자본잠식)의 부채비율과 ROE
import pandas as pd

pd.set_option("display.unicode.east_asian_width", True)
FILE = "../data/상장사_재무_2021_2025.xlsx"
df25 = pd.read_excel(FILE, sheet_name="2025", dtype={"종목코드": str})

df25["부채비율"] = df25["부채총계"] / df25["자본총계"]
df25["ROE"] = df25["당기순이익"] / df25["자본총계"]

neg = df25[df25["자본총계"] < 0]
print(len(neg), df25["자본총계"].isna().sum())
cols = ["회사명", "부채총계", "자본총계", "당기순이익", "부채비율", "ROE"]
print(neg[cols].sort_values("자본총계").round(2).to_string(index=False))
print((neg["당기순이익"] < 0).sum(), (neg["ROE"] > 0).sum())   # 손실인 곳, ROE가 양수인 곳
