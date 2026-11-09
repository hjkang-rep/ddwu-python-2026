# 막대 그래프로 업종별 비교: 2025년 매출액 합계 상위 10개
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

s = df25.groupby("업종")["매출액"].sum() / 1_000_000    # 업종마다 합계, 조 원
print(len(s))
top = s.sort_values(ascending=False).head(10)
print(top.round(1))

fig, ax = plt.subplots(figsize=(4.8, 3.2))
bars = ax.barh(top.index, top.values, color="#2a78d6")
ax.invert_yaxis()                  # 큰 값이 맨 위로
ax.bar_label(bars, fmt="%.1f", padding=2)           # 막대 끝에 값 표시
ax.set_xlim(0, 560)
ax.set_title("2025년 업종별 매출액 합계 상위 10개")
ax.set_xlabel("조 원")
plt.savefig("../내작업/p13_업종상위10.png", dpi=150, bbox_inches="tight")
print("저장 완료")
