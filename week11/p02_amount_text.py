# 금액 열의 자료형 확인: 쉼표가 있는 문자열
import pandas as pd

FILE = "../data/상장사_재무_원자료_2025.xlsx"
raw = pd.read_excel(FILE, sheet_name="원자료", dtype=str)

amt = raw["thstrm_amount"]
print(amt.dtype)
print(amt.head(3).tolist())
print(amt.head(3).sum())      # 문자열끼리 더하면 글자가 이어 붙음
print(amt.sort_values(ascending=False).head(3).tolist())   # 글자 순서로 정렬됨
