# 첫 그래프: 삼성전자 매출액 5년 (한글 폰트 설정, 파일로 저장)
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import font_manager

font_manager.fontManager.addfont("../data/fonts/NanumGothic.ttf")
plt.rcParams["font.family"] = "NanumGothic"
plt.rcParams["axes.unicode_minus"] = False        # 음수 부호가 네모로 나오지 않게

FILE = "../data/상장사_재무_2021_2025.xlsx"
years = ["2021", "2022", "2023", "2024", "2025"]
books = pd.read_excel(FILE, sheet_name=years)      # 연도 시트 다섯 개를 딕셔너리로

sales = []
for y in years:
    d = books[y]
    v = d[d["회사명"] == "삼성전자"]["매출액"].iloc[0]   # 그해 삼성전자의 매출액 하나
    sales.append(v / 1_000_000)                        # 백만 원 -> 조 원
print(pd.Series(sales).round(1).tolist())

fig, ax = plt.subplots(figsize=(4.8, 3))
ax.plot(years, sales, marker="o", color="#2a78d6")
ax.set_title("삼성전자 매출액")
ax.set_xlabel("사업연도")
ax.set_ylabel("조 원")
plt.savefig("../내작업/p10_삼성전자.png", dpi=150, bbox_inches="tight")
print("저장 완료")
