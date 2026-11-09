# 빈칸이 선 그래프에 주는 영향: 카카오의 2021, 2022년 매출액
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import font_manager

font_manager.fontManager.addfont("../data/fonts/NanumGothic.ttf")
plt.rcParams["font.family"] = "NanumGothic"
plt.rcParams["axes.unicode_minus"] = False

FILE = "../data/상장사_재무_2021_2025.xlsx"
years = ["2021", "2022", "2023", "2024", "2025"]
books = pd.read_excel(FILE, sheet_name=years)
colors = {"NAVER": "#2a78d6", "카카오": "#eb6834"}

fig, ax = plt.subplots(figsize=(4.8, 3))
for name, c in colors.items():
    sales = []
    for y in years:
        d = books[y]
        v = d[d["회사명"] == name]["매출액"].iloc[0]       # 빈칸이면 NaN
        sales.append(v / 1_000_000)
    print(name, pd.Series(sales).round(1).tolist())
    ax.plot(years, sales, marker="o", color=c, label=name)

ax.set_title("NAVER와 카카오의 매출액")
ax.set_ylabel("매출액 (조 원)")
ax.set_ylim(0, 14)
ax.legend()
ax.grid(axis="y", alpha=0.3)
plt.savefig("../내작업/p18_빈칸선.png", dpi=150, bbox_inches="tight")
print("저장 완료")
