# 업종마다 그림 파일 하나씩 저장: 매출액 상위 5개 회사
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import font_manager

font_manager.fontManager.addfont("../data/fonts/NanumGothic.ttf")
plt.rcParams["font.family"] = "NanumGothic"
plt.rcParams["axes.unicode_minus"] = False

FILE = "../data/상장사_재무_2021_2025.xlsx"
df = pd.read_excel(FILE, sheet_name="2025", dtype={"종목코드": str})
info = pd.read_excel(FILE, sheet_name="회사정보", dtype={"종목코드": str})
df25 = df.merge(info[["종목코드", "업종"]], on="종목코드", how="left")

for name in ["의약품 제조업", "반도체 제조업", "1차 철강 제조업"]:
    top = df25[df25["업종"] == name].sort_values("매출액", ascending=False).head(5)
    fig, ax = plt.subplots(figsize=(4.8, 2.6))
    ax.barh(top["회사명"], top["매출액"] / 1_000_000, color="#2a78d6")    # 백만 원 -> 조 원
    ax.invert_yaxis()
    ax.set_title(f"2025년 {name} 매출액 상위 5개")
    ax.set_xlabel("조 원")
    path = f"../내작업/p17_{name}.png"
    plt.savefig(path, dpi=150, bbox_inches="tight")
    plt.close(fig)                                # 다 쓴 그림은 닫음
    print(path)
