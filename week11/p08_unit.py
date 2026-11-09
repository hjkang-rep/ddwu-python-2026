# 원을 억 원으로 바꾸고 쉼표로 표시
import pandas as pd

pd.set_option("display.unicode.east_asian_width", True)

FILE = "../data/상장사_재무_원자료_2025.xlsx"
raw = pd.read_excel(FILE, sheet_name="원자료", dtype=str)
raw["당기"] = pd.to_numeric(raw["thstrm_amount"].str.replace(",", "", regex=False), errors="coerce")
cfs_codes = raw[raw["fs_div"] == "CFS"]["stock_code"].unique()
df = raw[(raw["fs_div"] == "CFS") | (~raw["stock_code"].isin(cfs_codes))]
clean = df.drop_duplicates(subset=["stock_code", "fs_div", "account_nm"], keep="first")
wide = clean.pivot(index=["stock_code", "회사명", "fs_div"], columns="account_nm", values="당기").reset_index()
wide.columns.name = None

eok = wide[["회사명", "매출액", "영업이익"]].copy()
for a in ["매출액", "영업이익"]:
    eok[a] = (eok[a] / 100_000_000).round(0)      # 원 -> 억 원
top = eok.sort_values("매출액", ascending=False).head(3)
print(top)                                        # 기본 표시

pd.set_option("display.float_format", "{:,.0f}".format)
print(top)                                        # 쉼표 표시, 값은 그대로

top["매출액_표시"] = top["매출액"].map("{:,.0f}억 원".format)
print(top[["회사명", "매출액_표시"]])
print(top["매출액"].dtype, top["매출액_표시"].dtype)
