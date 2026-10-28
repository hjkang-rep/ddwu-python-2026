# groupby: 묶을 열 · 계산할 열 · 계산 방법
import pandas as pd
pd.set_option("display.unicode.east_asian_width", True)  # 한글이 섞인 표의 열을 맞춤

df = pd.read_excel("매출대장_9월.xlsx", header=2)
done = df[df["상태"] == "완료"]
print(done.groupby("분류")["금액"].sum())
print(done.groupby("분류")["금액"].mean().round())
print(done.groupby("분류")["주문번호"].count())
summary = done.groupby("상품명").agg(건수=("주문번호", "count"), 수량=("수량", "sum"), 매출=("금액", "sum"))
print(summary.sort_values("매출", ascending=False))
