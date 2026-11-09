# 지주회사의 연결 매출 겹침이 업종 순위에 주는 영향
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

s = df25.groupby("업종")["매출액"].sum() / 1_000_000
top = s.sort_values(ascending=False).head(6)
top2 = s.drop("기타 금융업").sort_values(ascending=False).head(6)
print(top.round(1))
print(top2.round(1))
h = df25[df25["업종"] == "기타 금융업"].sort_values("매출액", ascending=False)
print(h[["회사명", "매출액"]].head(6))

fig, axes = plt.subplots(1, 2, figsize=(8, 2.6))
axes[0].barh(top.index, top.values, color="#2a78d6")
axes[0].invert_yaxis()
axes[0].set_title("2025년 업종별 매출액 합계 상위 6개")
axes[0].set_xlabel("조 원")
axes[1].barh(top2.index, top2.values, color="#2a78d6")
axes[1].invert_yaxis()
axes[1].set_title("2025년 업종별 매출액 합계 (기타 금융업 제외)")
axes[1].set_xlabel("조 원")
plt.tight_layout()
plt.savefig("../내작업/p21_지주회사.png", dpi=150, bbox_inches="tight")
print("저장 완료")
