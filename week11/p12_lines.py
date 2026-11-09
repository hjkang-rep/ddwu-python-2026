# 선 그래프로 회사별 추이: 자동차 세 회사의 매출액
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import font_manager

font_manager.fontManager.addfont("../data/fonts/NanumGothic.ttf")
plt.rcParams["font.family"] = "NanumGothic"
plt.rcParams["axes.unicode_minus"] = False

FILE = "../data/상장사_재무_2021_2025.xlsx"
years = ["2021", "2022", "2023", "2024", "2025"]
books = pd.read_excel(FILE, sheet_name=years)
colors = {"현대자동차": "#2a78d6", "기아": "#eb6834", "현대모비스": "#1baf7a"}

fig, ax = plt.subplots(figsize=(4.8, 3))
for name, c in colors.items():
    sales = []
    for y in years:
        d = books[y]
        v = d[d["회사명"] == name]["매출액"].iloc[0]
        sales.append(v / 1_000_000)
    print(name, pd.Series(sales).round(1).tolist())
    ax.plot(years, sales, marker="o", color=c, label=name)

ax.set_title("자동차 세 회사의 매출액")
ax.set_xlabel("사업연도")
ax.set_ylabel("매출액 (조 원)")
ax.set_ylim(0, 220)
ax.legend(loc="upper left", ncol=3)
ax.grid(axis="y", alpha=0.3)
plt.savefig("../내작업/p12_자동차.png", dpi=150, bbox_inches="tight")
print("저장 완료")
