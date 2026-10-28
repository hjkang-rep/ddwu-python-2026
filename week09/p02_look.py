# 표를 처음 받았을 때 보는 네 가지: 크기 · 앞 · 뒤 · 열의 자료형
import pandas as pd
pd.set_option("display.unicode.east_asian_width", True)  # 한글이 섞인 표의 열을 맞춤

df = pd.read_excel("매출대장_9월.xlsx", header=2)
print(df.shape)
print(df.tail(2))
print(df.dtypes)
