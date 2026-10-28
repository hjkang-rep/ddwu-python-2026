# 값마다 몇 번 나오나: value_counts. 지점 이름을 세어 보면
import pandas as pd
pd.set_option("display.unicode.east_asian_width", True)  # 한글이 섞인 표의 열을 맞춤

df = pd.read_excel("매출대장_9월.xlsx", header=2)
print(df["지점"].value_counts())
print(df["지점"].unique())
df["지점"] = df["지점"].str.strip()
print(df["지점"].value_counts())
