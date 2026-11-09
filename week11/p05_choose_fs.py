# 연결재무제표가 있으면 연결, 없으면 별도 고르기
import pandas as pd

FILE = "../data/상장사_재무_원자료_2025.xlsx"
raw = pd.read_excel(FILE, sheet_name="원자료", dtype=str)

cfs_codes = raw[raw["fs_div"] == "CFS"]["stock_code"].unique()   # 연결이 있는 회사의 종목코드
print(len(cfs_codes))

keep = (raw["fs_div"] == "CFS") | (~raw["stock_code"].isin(cfs_codes))
df = raw[keep]
print(len(raw), len(df))
print(df.groupby("fs_div")["stock_code"].nunique())
