# 내가 정리한 표와 정리본(2025 시트)을 칸마다 대조
import pandas as pd

pd.set_option("display.unicode.east_asian_width", True)

FILE = "../data/상장사_재무_원자료_2025.xlsx"
CLEAN = "../data/상장사_재무_2021_2025.xlsx"
ACCOUNTS = ["매출액", "영업이익", "법인세차감전순이익", "당기순이익", "자산총계", "부채총계", "자본총계",
            "유동자산", "유동부채", "자본금", "이익잉여금"]

# 원자료 정리
raw = pd.read_excel(FILE, sheet_name="원자료", dtype=str)
raw["당기"] = pd.to_numeric(raw["thstrm_amount"].str.replace(",", "", regex=False), errors="coerce")
cfs_codes = raw[raw["fs_div"] == "CFS"]["stock_code"].unique()
df = raw[(raw["fs_div"] == "CFS") | (~raw["stock_code"].isin(cfs_codes))]
clean = df.drop_duplicates(subset=["stock_code", "fs_div", "account_nm"], keep="first")
wide = clean.pivot(index=["stock_code", "회사명", "fs_div"], columns="account_nm", values="당기").reset_index()
wide.columns.name = None
wide = wide.rename(columns={"법인세차감전 순이익": "법인세차감전순이익", "당기순이익(손실)": "당기순이익"})

# 정리본과 같은 모양으로: 백만 원, 열 이름, 재무제표 표기
my = wide.rename(columns={"stock_code": "종목코드"})
for col in ACCOUNTS:
    my[col] = (my[col] / 1_000_000).round(0)
my["재무제표"] = my["fs_div"].map({"CFS": "연결", "OFS": "별도"})
my = my[["종목코드", "회사명", "재무제표"] + ACCOUNTS]

# 정리본의 2025 시트에서 유가증권시장 회사만
book = pd.read_excel(CLEAN, sheet_name=["회사정보", "2025"], dtype={"종목코드": str})
info = book["회사정보"]
kospi = info[info["시장"] == "유가증권"]["종목코드"]
target = book["2025"][book["2025"]["종목코드"].isin(kospi)]
print(my.shape, target.shape)

# 종목코드 순서로 맞춘 뒤 칸마다 비교
left = my.sort_values("종목코드").reset_index(drop=True)
right = target.sort_values("종목코드").reset_index(drop=True)
print((left["종목코드"] == right["종목코드"]).all())
diff = left.compare(right)
print(diff.shape)
print(left[left["회사명"] == "삼성전자"][["회사명", "재무제표", "매출액", "영업이익"]])
print(right[right["회사명"] == "삼성전자"][["회사명", "재무제표", "매출액", "영업이익"]])
