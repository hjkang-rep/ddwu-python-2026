# 순위와 구간: rank · nlargest · nsmallest · pd.cut
import numpy as np
import pandas as pd

pd.set_option("display.unicode.east_asian_width", True)
FILE = "../data/상장사_재무_2021_2025.xlsx"
df = pd.read_excel(FILE, sheet_name="2025", dtype={"종목코드": str})
info = pd.read_excel(FILE, sheet_name="회사정보", dtype={"종목코드": str})
df25 = df.merge(info[["종목코드", "업종"]], on="종목코드", how="left")
sales = df25["매출액"].where(df25["매출액"] > 0)
df25["영업이익률"] = df25["영업이익"] / sales

ph = df25[df25["업종"] == "의약품 제조업"].copy()
ph["매출순위"] = ph["매출액"].rank(ascending=False, method="min")      # 큰 값이 1위
ph["이익률순위"] = ph["영업이익률"].rank(ascending=False, method="min")
cols = ["회사명", "매출액", "매출순위", "영업이익률", "이익률순위"]
print(ph.nlargest(5, "매출액")[cols].round(3))
print(ph.nlargest(3, "영업이익률")[cols].round(3))
print(ph.nsmallest(3, "영업이익률")[cols].round(3))

bins = [-np.inf, 0, 0.05, 0.10, np.inf]
labels = ["손실", "0~5%", "5~10%", "10% 이상"]
ph["이익률구간"] = pd.cut(ph["영업이익률"], bins=bins, labels=labels, right=False)
print(ph["이익률구간"].value_counts(sort=False))

# 업종 안에서의 순위: groupby 뒤에 rank
df25["업종내매출순위"] = df25.groupby("업종")["매출액"].rank(ascending=False, method="min")
print(df25[df25["회사명"].isin(["삼성전자", "유한양행", "SK하이닉스"])]
      [["회사명", "업종", "업종내매출순위"]])
