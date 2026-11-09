# 긴 표(회사 · 계정마다 한 행)를 넓은 표(회사마다 한 행)로
import pandas as pd

pd.set_option("display.unicode.east_asian_width", True)

FILE = "../data/상장사_재무_원자료_2025.xlsx"
raw = pd.read_excel(FILE, sheet_name="원자료", dtype=str)
raw["당기"] = pd.to_numeric(raw["thstrm_amount"].str.replace(",", "", regex=False), errors="coerce")
cfs_codes = raw[raw["fs_div"] == "CFS"]["stock_code"].unique()
df = raw[(raw["fs_div"] == "CFS") | (~raw["stock_code"].isin(cfs_codes))]
clean = df.drop_duplicates(subset=["stock_code", "fs_div", "account_nm"], keep="first")

wide = clean.pivot(index=["stock_code", "회사명", "fs_div"], columns="account_nm", values="당기")
print(wide.shape)

wide = wide.reset_index()
wide.columns.name = None        # 표 왼쪽 위에 남는 이름표(account_nm)를 지움
wide = wide.rename(columns={"법인세차감전 순이익": "법인세차감전순이익", "당기순이익(손실)": "당기순이익"})
ACCOUNTS = ["매출액", "영업이익", "법인세차감전순이익", "당기순이익", "자산총계", "부채총계", "자본총계",
            "유동자산", "유동부채", "자본금", "이익잉여금"]
wide = wide[["stock_code", "회사명", "fs_div"] + ACCOUNTS]
print(wide.shape)
print(wide[["회사명", "fs_div", "매출액", "영업이익"]].head(3))
