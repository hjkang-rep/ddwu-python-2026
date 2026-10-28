# 정렬과 상위 n개
import pandas as pd
pd.set_option("display.unicode.east_asian_width", True)  # 한글이 섞인 표의 열을 맞춤

df = pd.read_excel("매출대장_9월.xlsx", header=2)
done = df[df["상태"] == "완료"]
top = done.sort_values("금액", ascending=False)
print(top[["주문번호", "지점", "상품명", "수량", "금액"]].head(5))
