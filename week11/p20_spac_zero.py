# 스팩의 매출액 0이 중앙값 막대에 주는 영향
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import font_manager

font_manager.fontManager.addfont("../data/fonts/NanumGothic.ttf")
plt.rcParams["font.family"] = "NanumGothic"
plt.rcParams["axes.unicode_minus"] = False
pd.set_option("display.unicode.east_asian_width", True)

FILE = "../data/상장사_재무_2021_2025.xlsx"
df = pd.read_excel(FILE, sheet_name="2025", dtype={"종목코드": str})
info = pd.read_excel(FILE, sheet_name="회사정보", dtype={"종목코드": str})
df25 = df.merge(info[["종목코드", "업종"]], on="종목코드", how="left")

names = ["금융 지원 서비스업", "기타 금융업", "의약품 제조업", "소프트웨어 개발 및 공급업", "반도체 제조업"]
d = df25[df25["업종"].isin(names)]
no_spac = d[~d["회사명"].str.contains("스팩")]

a = d.groupby("업종")["매출액"].median() / 1_000_000       # 백만 원 -> 조 원
b = no_spac.groupby("업종")["매출액"].median() / 1_000_000
print(a.round(2))
print(b.round(2))
f = d[d["업종"] == "금융 지원 서비스업"]
print(len(f), f["회사명"].str.contains("스팩").sum(), (f["매출액"] == 0).sum(), f["매출액"].isna().sum())

fig, axes = plt.subplots(1, 2, figsize=(8, 2.6), sharex=True, sharey=True)
order = b.sort_values(ascending=False).index
b0 = axes[0].barh(order, a[order], color="#2a78d6")
axes[0].bar_label(b0, fmt="%.2f", padding=2)
axes[0].invert_yaxis()
axes[0].set_title("매출액 중앙값: 스팩 포함")
b1 = axes[1].barh(order, b[order], color="#2a78d6")
axes[1].bar_label(b1, fmt="%.2f", padding=2)
axes[1].set_xlim(0, 2.1)
axes[1].set_title("매출액 중앙값: 스팩 제외")
axes[0].set_xlabel("조 원")
axes[1].set_xlabel("조 원")
plt.tight_layout()
plt.savefig("../내작업/p20_스팩.png", dpi=150, bbox_inches="tight")
print("저장 완료")
