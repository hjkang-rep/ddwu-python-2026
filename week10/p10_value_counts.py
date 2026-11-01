# 범주별 개수: value_counts
import pandas as pd

pd.set_option("display.unicode.east_asian_width", True)
info = pd.read_excel("../data/상장사_재무_2021_2025.xlsx", sheet_name="회사정보")
print(info["시장"].value_counts())
print(info["업종"].value_counts().head(8))
print(info["결산월"].value_counts().head(4))
