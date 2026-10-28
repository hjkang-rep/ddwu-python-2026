# 열 꺼내기: 한 열은 Series, 여러 열은 DataFrame
import pandas as pd
pd.set_option("display.unicode.east_asian_width", True)  # 한글이 섞인 표의 열을 맞춤

df = pd.read_excel("매출대장_9월.xlsx", header=2)
amount = df["금액"]
print(type(amount).__name__, len(amount))
print(amount.head(3))
print(df[["지점", "상품명", "금액"]].head(3))
print(df["금액"].sum(), df["수량"].max())
