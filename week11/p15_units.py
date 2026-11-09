# 단위: 백만 원 그대로 그린 축과 조 원으로 나눠 그린 축
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import font_manager

font_manager.fontManager.addfont("../data/fonts/NanumGothic.ttf")
plt.rcParams["font.family"] = "NanumGothic"
plt.rcParams["axes.unicode_minus"] = False

FILE = "../data/상장사_재무_2021_2025.xlsx"
years = ["2021", "2022", "2023", "2024", "2025"]
books = pd.read_excel(FILE, sheet_name=years)

sales = []
for y in years:
    d = books[y]
    sales.append(d[d["회사명"] == "삼성전자"]["매출액"].iloc[0])     # 백만 원 그대로

fig, axes = plt.subplots(1, 2, figsize=(8, 3))                     # 축 두 개를 나란히
axes[0].plot(years, sales, marker="o", color="#2a78d6")
axes[0].set_title("백만 원 그대로, 단위 없음")

axes[1].plot(years, [s / 1_000_000 for s in sales], marker="o", color="#2a78d6")
axes[1].set_title("조 원으로 나눔, 축에 단위 표시")
axes[1].set_ylabel("매출액 (조 원)")
axes[1].set_ylim(0, 400)                                           # 축을 0부터
axes[1].grid(axis="y", alpha=0.3)
plt.tight_layout()                                                  # 축끼리 겹치지 않게
plt.savefig("../내작업/p15_단위.png", dpi=150, bbox_inches="tight")
print("저장 완료")
