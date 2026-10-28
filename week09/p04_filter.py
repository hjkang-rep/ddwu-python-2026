# 조건으로 행 고르기: 비교식이 True/False 열을 만들고, 그 열로 행을 고름
import pandas as pd
pd.set_option("display.unicode.east_asian_width", True)  # 한글이 섞인 표의 열을 맞춤

df = pd.read_excel("매출대장_9월.xlsx", header=2)
mask = df["상태"] == "완료"
print(mask.head(3))
print(mask.sum())
done = df[mask]
print(done.shape)
big = df[(df["지점"] == "강남점") & (df["수량"] >= 5)]
print(big.shape)
print(big[["날짜", "상품명", "수량", "금액"]].head(3))
