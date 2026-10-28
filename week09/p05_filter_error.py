# 괄호 없이 &를 쓰면: 연산 순서 때문에 오류
import pandas as pd
pd.set_option("display.unicode.east_asian_width", True)  # 한글이 섞인 표의 열을 맞춤

df = pd.read_excel("매출대장_9월.xlsx", header=2)
big = df[df["지점"] == "강남점" & df["수량"] >= 5]
