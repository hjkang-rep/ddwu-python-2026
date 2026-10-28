# 같은 집계를 두 가지로: 딕셔너리 누적 반복문과 groupby
import pandas as pd
pd.set_option("display.unicode.east_asian_width", True)  # 한글이 섞인 표의 열을 맞춤

df = pd.read_excel("매출대장_9월.xlsx", header=2)
done = df[df["상태"] == "완료"]

names = list(done["상품명"])
amounts = list(done["금액"])
totals = {}
for i in range(len(names)):
    totals[names[i]] = totals.get(names[i], 0) + amounts[i]
print(totals)

print(done.groupby("상품명")["금액"].sum())
