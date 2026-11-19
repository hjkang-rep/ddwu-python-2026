# 내 업종 보고서: 함수 두 개(summary, top5)로 시트 두 장짜리 엑셀을 만듦
import pandas as pd

pd.set_option("display.unicode.east_asian_width", True)
pd.set_option("display.float_format", "{:,.1f}".format)
FILE = "../data/상장사_재무_2021_2025.xlsx"
INDUSTRY = "의약품 제조업"   # 여기만 바꿈. 정확한 이름은 week12/find_industry.py로 찾음

df = pd.read_excel(FILE, sheet_name="2025", dtype={"종목코드": str})
info = pd.read_excel(FILE, sheet_name="회사정보", dtype={"종목코드": str})
df["영업이익률"] = df["영업이익"] / df["매출액"] * 100
ok = df[(df["매출액"] > 0) & df["영업이익"].notna()]
ok = ok.merge(info[["종목코드", "업종"]], on="종목코드")


def summary(industry):
    """업종 이름을 받아 회사 수 · 영업이익률 중앙값 · 적자 회사 비율을 표로 돌려줌"""
    mine = ok[ok["업종"] == industry]
    n = len(mine)
    median = mine["영업이익률"].median()
    loss = (mine["영업이익"] < 0).sum() / n * 100
    return pd.DataFrame({
        "업종": [industry],
        "회사 수": [n],
        "영업이익률 중앙값(%)": [round(median, 1)],
        "적자 회사 비율(%)": [round(loss, 1)],
    })


def top5(industry):
    """업종 이름을 받아 영업이익률 상위 5개 회사 표를 돌려줌"""
    mine = ok[ok["업종"] == industry]
    top = mine.sort_values("영업이익률", ascending=False).head(5)
    return top[["회사명", "매출액", "영업이익", "영업이익률"]].round(1)


s = summary(INDUSTRY)
t = top5(INDUSTRY)
print(INDUSTRY)
print(s.to_string(index=False))
print(t.to_string(index=False))

writer = pd.ExcelWriter("../내작업/w13_보고서.xlsx")
s.to_excel(writer, sheet_name="요약", index=False)
t.to_excel(writer, sheet_name="상위5", index=False)
writer.close()
print("저장 완료: 내작업/w13_보고서.xlsx")
