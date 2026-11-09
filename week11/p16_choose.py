# 업종 비교를 선으로 그린 그림과 막대로 그린 그림
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

names = ["의약품 제조업", "반도체 제조업", "1차 철강 제조업", "전자부품 제조업", "소프트웨어 개발 및 공급업"]
s = df25[df25["업종"].isin(names)].groupby("업종")["매출액"].sum() / 1_000_000
print(s.round(1))

fig, axes = plt.subplots(1, 2, figsize=(8, 3))
axes[0].plot(s.index, s.values, marker="o", color="#2a78d6")         # 가나다순으로 이은 선
axes[0].set_title("선으로 그림: 순서 없는 업종을 이음")
axes[0].tick_params(axis="x", labelrotation=30)

t = s.sort_values(ascending=False)
axes[1].barh(t.index, t.values, color="#2a78d6")
axes[1].invert_yaxis()
axes[1].set_title("막대로 그림: 큰 순서로 정렬")
axes[1].set_xlabel("조 원")
plt.tight_layout()
plt.savefig("../내작업/p16_그래프고르기.png", dpi=150, bbox_inches="tight")
print("저장 완료")
