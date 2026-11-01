# 요약표 두 개를 시트 두 개로 저장: ExcelWriter
import pandas as pd

FILE = "../data/상장사_재무_2021_2025.xlsx"
df = pd.read_excel(FILE, sheet_name="2025")
info = pd.read_excel(FILE, sheet_name="회사정보")
df25 = df.merge(info[["종목코드", "시장", "업종"]], on="종목코드", how="left")
market = df25.groupby("시장")["매출액"].agg(["count", "sum", "median"])
industry = df25.groupby("업종").agg(회사수=("회사명", "count"), 매출합계=("매출액", "sum"))
with pd.ExcelWriter("../내작업/요약_2025.xlsx") as writer:
    market.to_excel(writer, sheet_name="시장")
    industry.sort_values("매출합계", ascending=False).to_excel(writer, sheet_name="업종")
print("저장 완료:", market.shape, industry.shape)
