# 쉼표 금액을 숫자로 바꾸고 바뀌지 않은 값을 확인
import pandas as pd

pd.set_option("display.unicode.east_asian_width", True)

FILE = "../data/상장사_재무_원자료_2025.xlsx"
raw = pd.read_excel(FILE, sheet_name="원자료", dtype=str)

txt = raw["thstrm_amount"].str.replace(",", "", regex=False)
num = pd.to_numeric(txt, errors="coerce")     # 숫자로 못 바꾼 칸은 NaN
print(num.dtype, num.notna().sum(), num.isna().sum())

fail = raw[num.isna()]                        # 바뀌지 않은 행의 원래 글자
print(fail["thstrm_amount"].value_counts())
print(fail[["회사명", "fs_div", "account_nm", "thstrm_amount"]].head(3))

raw["당기"] = num
sam = raw[(raw["회사명"] == "삼성전자") & (raw["account_nm"] == "매출액")]
print(sam[["fs_div", "thstrm_amount", "당기"]])
