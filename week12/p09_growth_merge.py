# 두 해를 merge로 붙여 성장률 계산: 전년 행이 없는 회사 확인
import pandas as pd

pd.set_option("display.unicode.east_asian_width", True)
FILE = "../data/상장사_재무_2021_2025.xlsx"
books = pd.read_excel(FILE, sheet_name=["2024", "2025"], dtype={"종목코드": str})
y24 = books["2024"][["종목코드", "매출액"]].rename(columns={"매출액": "전년매출액"})
y25 = books["2025"][["종목코드", "회사명", "매출액"]]

m = y25.merge(y24, on="종목코드", how="left", indicator=True)  # 2025년 회사는 모두 남김
print(len(y25), len(y24), len(m))
print(m["_merge"].value_counts())

m["매출성장률"] = m["매출액"] / m["전년매출액"] - 1
print(m[m["회사명"] == "삼성전자"].round(4).to_string(index=False))

# 성장률이 빈칸인 이유 세기
no_row = m["_merge"] == "left_only"                          # 2024년 시트에 행이 없음
prev_na = ~no_row & m["전년매출액"].isna()                   # 전년 매출액 빈칸
this_na = ~no_row & m["전년매출액"].notna() & m["매출액"].isna()  # 올해 매출액 빈칸
zero = (m["전년매출액"] == 0) & (m["매출액"] == 0)          # 0 / 0
print("빈칸", m["매출성장률"].isna().sum())
print(no_row.sum(), prev_na.sum(), this_na.sum(), zero.sum())
print("inf", ((m["전년매출액"] == 0) & (m["매출액"] > 0)).sum())
