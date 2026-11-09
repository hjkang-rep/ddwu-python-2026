# 정렬하지 않고 앞 10개를 그리면: 가나다순의 앞 10개 업종이 나옴
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

first = s.head(10)                                # 정렬 없이 앞 10개
print(first.round(1))

fig, ax = plt.subplots(figsize=(4.8, 3.2))
ax.barh(first.index, first.values, color="#2a78d6")
ax.invert_yaxis()
ax.set_title("정렬하지 않은 앞 10개 업종")
ax.set_xlabel("조 원")
plt.savefig("../내작업/p14_정렬없음.png", dpi=150, bbox_inches="tight")
print("저장 완료")
