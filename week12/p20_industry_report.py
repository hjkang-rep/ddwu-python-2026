# 업종 보고서 엑셀: 업종 이름을 넣으면 요약 · 회사별 · 연도별 추이 시트와 그림이 든 통합 문서를 만듦
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib import font_manager
from openpyxl import load_workbook
from openpyxl.drawing.image import Image
from openpyxl.styles import Alignment, Font, PatternFill

font_manager.fontManager.addfont("../data/fonts/NanumGothic.ttf")
plt.rcParams["font.family"] = "NanumGothic"
plt.rcParams["axes.unicode_minus"] = False
pd.set_option("display.unicode.east_asian_width", True)

INDUSTRY = "의약품 제조업"          # 이 줄만 바꾸면 다른 업종의 보고서
AUTHOR = "Hojun Kang"               # 문서 속성에 들어갈 작성자 이름
YEAR = 2025
FILE = "../data/상장사_재무_2021_2025.xlsx"
OUT = f"../내작업/업종보고서_{INDUSTRY}.xlsx"
PNG = f"../내작업/업종보고서_{INDUSTRY}.png"
years = ["2021", "2022", "2023", "2024", "2025"]

# 1. 읽기: 연도 시트 다섯 개를 긴 표 하나로 붙이고 업종을 붙임
books = pd.read_excel(FILE, sheet_name=None, dtype={"종목코드": str})
info = books["회사정보"]
parts = []
for y in years:
    t = books[y].copy()
    t["연도"] = int(y)
    parts.append(t)
df = pd.concat(parts, ignore_index=True)
df = df.merge(info[["종목코드", "시장", "업종"]], on="종목코드", how="left")
d = df[df["업종"] == INDUSTRY].copy()
print(INDUSTRY, len(d), "행")

# 2. 지표: 분모가 0 이하이면 빈칸
sales = d["매출액"].where(d["매출액"] > 0)
equity = d["자본총계"].where(d["자본총계"] > 0)
d["영업이익률"] = d["영업이익"] / sales
d["순이익률"] = d["당기순이익"] / sales
d["부채비율"] = d["부채총계"] / equity
d["ROE"] = d["당기순이익"] / equity
d = d.sort_values(["종목코드", "연도"])
d["매출성장률"] = d.groupby("종목코드")["매출액"].pct_change()
d["매출성장률"] = d["매출성장률"].replace([np.inf, -np.inf], np.nan)
for c in ["매출액", "영업이익", "당기순이익"]:
    d[c + "(억 원)"] = d[c] / 100

# 3. 표 세 개
last = d[d["연도"] == YEAR].copy()
last["순위"] = last["매출액"].rank(ascending=False, method="min")
cols = ["순위", "회사명", "시장", "재무제표", "매출액(억 원)", "영업이익(억 원)", "당기순이익(억 원)",
        "영업이익률", "순이익률", "부채비율", "ROE", "매출성장률"]
firms = last.sort_values("매출액", ascending=False)[cols]

ok = d[d["영업이익률"].notna()].copy()   # 영업이익률을 계산할 수 있는 행만 합함
ok["손실"] = ok["영업이익"] < 0
trend = ok.groupby("연도").agg(회사수=("회사명", "count"),
                              매출액=("매출액(억 원)", "sum"),
                              영업이익=("영업이익(억 원)", "sum"),
                              중앙값=("영업이익률", "median"),
                              손실회사=("손실", "sum"))
trend["합계기준"] = trend["영업이익"] / trend["매출액"]
trend = trend.reset_index()
trend = trend[["연도", "회사수", "매출액", "영업이익", "합계기준", "중앙값", "손실회사"]]
trend.columns = ["연도", "회사 수", "매출액(억 원)", "영업이익(억 원)", "영업이익률(합계 기준)",
                 "영업이익률(중앙값)", "영업손실 회사 수"]

t25 = trend[trend["연도"] == YEAR].iloc[0]
markets = last["시장"].value_counts()
summary = pd.DataFrame({
    "항목": ["업종", "사업연도", "회사 수", "유가증권시장 · 코스닥",
             "매출액 합계(억 원)", "영업이익 합계(억 원)", "영업이익률(합계 기준)", "영업이익률(중앙값)",
             "영업손실 회사 수", "자본잠식 회사 수", "매출액 1위", "영업이익률 1위",
             "자료", "영업이익률", "순이익률", "부채비율", "ROE", "매출성장률"],
    "값": [INDUSTRY, YEAR, len(last), f"{markets.get('유가증권', 0)} · {markets.get('코스닥', 0)}",
          t25["매출액(억 원)"], t25["영업이익(억 원)"], t25["영업이익률(합계 기준)"], t25["영업이익률(중앙값)"],
          int((last["영업이익"] < 0).sum()), int((last["자본총계"] < 0).sum()),
          firms["회사명"].iloc[0], last.nlargest(1, "영업이익률")["회사명"].iloc[0],
          "OpenDART 사업보고서 주요계정, 한국거래소 상장법인목록 (2026-11-01 수집)",
          "영업이익 ÷ 매출액", "당기순이익 ÷ 매출액", "부채총계 ÷ 자본총계", "당기순이익 ÷ 자본총계",
          "올해 매출액 ÷ 전년 매출액 - 1 (매출액 · 자본총계가 0 이하이면 빈칸)"],
})

# 4. pandas로 값 저장
with pd.ExcelWriter(OUT) as writer:
    summary.to_excel(writer, sheet_name="요약", index=False)
    firms.to_excel(writer, sheet_name="회사별", index=False)
    trend.to_excel(writer, sheet_name="연도별 추이", index=False)

# 5. 그림을 PNG로
fig, axes = plt.subplots(1, 2, figsize=(8, 2.8))
x = trend["연도"].astype(str)
axes[0].bar(x, trend["매출액(억 원)"] / 10_000, color="#2a78d6")
axes[0].set_title("매출액 합계 (조 원)")
axes[1].plot(x, trend["영업이익률(합계 기준)"] * 100, marker="o", color="#2a78d6", label="합계 기준")
axes[1].plot(x, trend["영업이익률(중앙값)"] * 100, marker="o", color="#eb6834", label="중앙값")
axes[1].axhline(0, color="gray", linewidth=0.8)
axes[1].set_title("영업이익률 (%)")
axes[1].legend()
fig.suptitle(INDUSTRY)
plt.tight_layout()
plt.savefig(PNG, dpi=150, bbox_inches="tight")
plt.close(fig)

# 6. openpyxl로 서식
wb = load_workbook(OUT)
head_font = Font(bold=True, color="FFFFFF")
head_fill = PatternFill(fill_type="solid", fgColor="1F4E79")
red = Font(color="C00000")
ratios = ["영업이익률", "순이익률", "부채비율", "ROE", "매출성장률",
          "영업이익률(합계 기준)", "영업이익률(중앙값)"]
for ws in wb.worksheets:
    for cell in ws[1]:                               # 머리글
        cell.font = head_font
        cell.fill = head_fill
        cell.alignment = Alignment(horizontal="center")
    for col_cells in ws.iter_cols(min_row=1):       # 열마다
        name = str(col_cells[0].value)
        letter = col_cells[0].column_letter
        ws.column_dimensions[letter].width = max(10, len(name) * 1.8 + 2)
        if "억 원" in name:
            fmt = "#,##0"
        elif name in ratios:
            fmt = "0.0%"
        else:
            fmt = None
        for cell in col_cells[1:]:
            if fmt is not None:
                cell.number_format = fmt
            if fmt is not None and cell.value is not None and cell.value < 0:
                cell.font = red                      # 음수(손실 · 감소)는 빨강

ws = wb["요약"]                                      # 요약 시트는 행마다 형식이 다름
ws.column_dimensions["A"].width = 24
ws.column_dimensions["B"].width = 60
for row in range(2, ws.max_row + 1):
    label = ws.cell(row=row, column=1).value
    cell = ws.cell(row=row, column=2)
    cell.alignment = Alignment(horizontal="left")
    if "억 원" in label:
        cell.number_format = "#,##0"
    elif label.startswith("영업이익률("):
        cell.number_format = "0.0%"
wb["회사별"].column_dimensions["B"].width = 24
wb["회사별"].freeze_panes = "C2"                     # 머리글과 순위 · 회사명 고정
wb["연도별 추이"].freeze_panes = "B2"

img = Image(PNG)                                     # 7. 그림 넣기
img.width, img.height = img.width * 0.55, img.height * 0.55
wb["연도별 추이"].add_image(img, "A9")

wb.properties.creator = AUTHOR                       # 8. 문서 속성
wb.properties.lastModifiedBy = AUTHOR
wb.properties.title = f"{INDUSTRY} 보고서"
wb.save(OUT)

print(summary.iloc[:12].to_string(index=False))
print("저장 완료:", OUT)
print(wb.sheetnames)
