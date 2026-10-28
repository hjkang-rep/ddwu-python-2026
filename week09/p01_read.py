# 엑셀 파일 읽기: 제목 줄이 있는 대장을 그대로 읽으면 / 머리글 줄을 알려 주면
import pandas as pd
pd.set_option("display.unicode.east_asian_width", True)  # 한글이 섞인 표의 열을 맞춤

raw = pd.read_excel("매출대장_9월.xlsx")
print(raw.iloc[:3, :4])

df = pd.read_excel("매출대장_9월.xlsx", header=2)
print(df.shape)
print(df.head(3))
