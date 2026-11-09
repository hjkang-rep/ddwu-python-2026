# 같은 계정이 두 번 나오는 행 찾기와 지우기
import pandas as pd

pd.set_option("display.unicode.east_asian_width", True)

FILE = "../data/상장사_재무_원자료_2025.xlsx"
raw = pd.read_excel(FILE, sheet_name="원자료", dtype=str)
cfs_codes = raw[raw["fs_div"] == "CFS"]["stock_code"].unique()
df = raw[(raw["fs_div"] == "CFS") | (~raw["stock_code"].isin(cfs_codes))]

key = ["stock_code", "fs_div", "account_nm"]
print(df.duplicated().sum())                  # 행 전체가 같은 행
print(df.duplicated(subset=key).sum())        # 회사 · 재무제표 · 계정이 같은 행

both = df[df.duplicated(subset=key, keep=False)]   # 겹치는 행을 모두 표시
print(both["account_nm"].value_counts())
print(both[both["회사명"] == "삼성전자"][["fs_div", "account_nm", "thstrm_amount", "ord"]])
print(both.groupby(key)["thstrm_amount"].nunique().max())   # 1이면 두 행의 금액이 언제나 같음

clean = df.drop_duplicates(subset=key, keep="first")
print(len(df), len(clean))
