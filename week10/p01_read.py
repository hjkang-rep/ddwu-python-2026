# 상장사 재무 엑셀의 2025년 시트 읽기
import pandas as pd

df = pd.read_excel("../data/상장사_재무_2021_2025.xlsx", sheet_name="2025")
print(df.shape)
print(df.columns.tolist())
