# 회사 이름으로 그 회사의 업종 이름 찾기 (m3_rank.py의 INDUSTRY에 그대로 복사)
import pandas as pd

pd.set_option("display.unicode.east_asian_width", True)
FILE = "../data/상장사_재무_2021_2025.xlsx"
COMPANY = "아모레퍼시픽"   # 여기만 바꿈

info = pd.read_excel(FILE, sheet_name="회사정보", dtype={"종목코드": str})
print(info[info["회사명"] == COMPANY][["회사명", "업종"]].to_string(index=False))
