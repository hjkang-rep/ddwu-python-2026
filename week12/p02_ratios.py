# 재무 지표 네 가지: 영업이익률 · 순이익률 · 부채비율 · ROE (2025년)
import pandas as pd

pd.set_option("display.unicode.east_asian_width", True)
FILE = "../data/상장사_재무_2021_2025.xlsx"
df25 = pd.read_excel(FILE, sheet_name="2025", dtype={"종목코드": str})

df25["영업이익률"] = df25["영업이익"] / df25["매출액"]
df25["순이익률"] = df25["당기순이익"] / df25["매출액"]
df25["부채비율"] = df25["부채총계"] / df25["자본총계"]
df25["ROE"] = df25["당기순이익"] / df25["자본총계"]

cols = ["영업이익률", "순이익률", "부채비율", "ROE"]
sam = df25[df25["회사명"] == "삼성전자"]
print(sam[["매출액", "영업이익", "당기순이익", "부채총계", "자본총계"]].T)
print(sam[cols].round(4))

names = ["삼성전자", "SK하이닉스", "현대자동차", "유한양행", "카카오뱅크"]
d = df25[df25["회사명"].isin(names)].set_index("회사명")
print((d[cols] * 100).round(1))                     # 보여 줄 때만 % 단위로
print(d["영업이익률"].map("{:.1%}".format).tolist())   # 글자로 바꾼 % 표시
