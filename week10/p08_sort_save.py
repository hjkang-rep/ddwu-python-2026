# 정렬과 상위 10개, 엑셀로 저장
import pandas as pd

pd.set_option("display.unicode.east_asian_width", True)
df = pd.read_excel("../data/상장사_재무_2021_2025.xlsx", sheet_name="2025")
top = df.sort_values("매출액", ascending=False).head(10)
print(top[["회사명", "매출액", "영업이익"]])
top.to_excel("../내작업/매출상위10_2025.xlsx", index=False)
print("저장 완료")
