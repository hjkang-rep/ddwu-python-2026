# 금융회사의 매출액 빈칸이 막대에 주는 영향: 매출액 합계와 당기순이익 합계
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import font_manager

font_manager.fontManager.addfont("../data/fonts/NanumGothic.ttf")
plt.rcParams["font.family"] = "NanumGothic"
plt.rcParams["axes.unicode_minus"] = False
pd.set_option("display.unicode.east_asian_width", True)
pd.set_option("display.float_format", "{:,.0f}".format)

FILE = "../data/상장사_재무_2021_2025.xlsx"
df = pd.read_excel(FILE, sheet_name="2025", dtype={"종목코드": str})
info = pd.read_excel(FILE, sheet_name="회사정보", dtype={"종목코드": str})
df25 = df.merge(info[["종목코드", "업종"]], on="종목코드", how="left")

names = ["보험업", "은행 및 저축기관"]
f = df25[df25["업종"].isin(names)]
t = f.groupby("업종").agg(회사수=("회사명", "count"), 매출있음=("매출액", "count"),
                          매출합계=("매출액", "sum"), 순이익합계=("당기순이익", "sum"))
print(t)

fig, axes = plt.subplots(1, 2, figsize=(8, 2.4), sharey=True)              # 두 축이 업종 이름을 같이 씀
b0 = axes[0].barh(t.index, t["매출합계"] / 1_000_000, color="#2a78d6")
axes[0].bar_label(b0, fmt="%.1f", padding=2)
axes[0].set_title("매출액 합계 (조 원)")
axes[0].set_xlim(0, 10)
b1 = axes[1].barh(t.index, t["순이익합계"] / 1_000_000, color="#2a78d6")
axes[1].bar_label(b1, fmt="%.1f", padding=2)
axes[1].set_title("당기순이익 합계 (조 원)")
axes[1].set_xlim(0, 10)
plt.tight_layout()
plt.savefig("../내작업/p19_금융빈칸.png", dpi=150, bbox_inches="tight")
print("저장 완료")
