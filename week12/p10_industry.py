# 업종 요약: 합계의 비율 · 비율의 평균 · 비율의 중앙값
import pandas as pd

pd.set_option("display.unicode.east_asian_width", True)
FILE = "../data/상장사_재무_2021_2025.xlsx"
df = pd.read_excel(FILE, sheet_name="2025", dtype={"종목코드": str})
info = pd.read_excel(FILE, sheet_name="회사정보", dtype={"종목코드": str})
df25 = df.merge(info[["종목코드", "업종"]], on="종목코드", how="left")
sales = df25["매출액"].where(df25["매출액"] > 0)
df25["영업이익률"] = df25["영업이익"] / sales

ph = df25[df25["업종"] == "의약품 제조업"]
print(len(ph), ph["영업이익률"].notna().sum())
print("합계의 비율  ", round(ph["영업이익"].sum() / ph["매출액"].sum(), 4))
print("비율의 평균  ", round(ph["영업이익률"].mean(), 4))
print("비율의 중앙값", round(ph["영업이익률"].median(), 4))
print(ph.sort_values("영업이익률")[["회사명", "매출액", "영업이익", "영업이익률"]].head(3).round(2))

# 업종마다: 영업이익률을 계산할 수 있는 회사만 써서 분자와 분모의 회사를 같게 함
base = df25[df25["영업이익률"].notna()]
s = base.groupby("업종").agg(
    회사수=("회사명", "count"),
    매출합계=("매출액", "sum"),
    영업이익합계=("영업이익", "sum"),
    평균=("영업이익률", "mean"),
    중앙값=("영업이익률", "median"),
)
s["합계기준"] = s["영업이익합계"] / s["매출합계"]
big = s[s["회사수"] >= 50].sort_values("합계기준", ascending=False)
print(len(big))
print((big[["합계기준", "평균", "중앙값"]] * 100).round(1).join(big["회사수"]))
