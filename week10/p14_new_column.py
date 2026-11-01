# 새 열 만들기와 비율: 영업손실 여부
import pandas as pd

pd.set_option("display.unicode.east_asian_width", True)
FILE = "../data/상장사_재무_2021_2025.xlsx"
df = pd.read_excel(FILE, sheet_name="2025")
info = pd.read_excel(FILE, sheet_name="회사정보")
df25 = df.merge(info[["종목코드", "시장", "업종"]], on="종목코드", how="left")
df25["영업손실"] = df25["영업이익"] < 0
print(df25["영업손실"].mean().round(3))
r = df25.groupby("업종").agg(회사수=("회사명", "count"), 손실비율=("영업손실", "mean"))
print(r[r["회사수"] >= 50].sort_values("손실비율", ascending=False).round(3).head(6))
