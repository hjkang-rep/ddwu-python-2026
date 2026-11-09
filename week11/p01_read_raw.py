# 공시 원자료 읽기: 크기, 열 이름, 회사 수
import pandas as pd

pd.set_option("display.unicode.east_asian_width", True)   # 한글이 섞인 표의 열을 맞춤

FILE = "../data/상장사_재무_원자료_2025.xlsx"
raw = pd.read_excel(FILE, sheet_name="원자료", dtype=str)   # 모든 열을 글자 그대로 읽음
print(raw.shape)
print(raw.columns.tolist())
print(raw["회사명"].nunique(), raw["account_nm"].nunique())
print(raw[["stock_code", "회사명", "fs_div", "account_nm", "thstrm_amount"]].head(3))
