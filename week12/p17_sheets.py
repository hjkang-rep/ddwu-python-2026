# 시트 여러 개: 요약 · 회사별 · 연도별 추이
import pandas as pd
from openpyxl import load_workbook

pd.set_option("display.unicode.east_asian_width", True)
FILE = "../data/상장사_재무_2021_2025.xlsx"
OUT = "../내작업/p17_시트.xlsx"
INDUSTRY = "의약품 제조업"
years = ["2021", "2022", "2023", "2024", "2025"]
books = pd.read_excel(FILE, sheet_name=None, dtype={"종목코드": str})
info = books["회사정보"]
codes = info[info["업종"] == INDUSTRY]["종목코드"]

parts = []
for y in years:
    t = books[y].copy()
    t["연도"] = int(y)
    parts.append(t)
df = pd.concat(parts, ignore_index=True)
d = df[df["종목코드"].isin(codes)].copy()           # 이 업종 회사의 5년 행
d["매출액"] = d["매출액"] / 100                       # 억 원
d["영업이익"] = d["영업이익"] / 100

trend = d.groupby("연도").agg(회사수=("회사명", "count"),
                             매출액=("매출액", "sum"))
print(trend.round(0))

firms = d[d["연도"] == 2025].sort_values("매출액", ascending=False)
firms = firms[["회사명", "매출액", "영업이익"]]
summary = pd.DataFrame({"항목": ["업종", "회사 수", "매출액 합계(억 원)"],
                        "값": [INDUSTRY, len(firms), firms["매출액"].sum()]})

with pd.ExcelWriter(OUT) as writer:                   # 쓰는 순서대로 시트가 놓임
    summary.to_excel(writer, sheet_name="요약", index=False)
    firms.to_excel(writer, sheet_name="회사별", index=False)
    trend.to_excel(writer, sheet_name="연도별 추이")    # 연도가 인덱스라 index를 남김

wb = load_workbook(OUT)
print(wb.sheetnames)
ws = wb.create_sheet("메모", 0)                       # 맨 앞(0번 자리)에 새 시트
ws["A1"] = "의약품 제조업 2025"
print(wb.sheetnames)
print(wb["연도별 추이"]["A1"].value, wb["연도별 추이"]["A2"].value, wb["연도별 추이"].max_row)
wb.save(OUT)
