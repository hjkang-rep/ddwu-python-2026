# 3단계: 업종 요약 함수 summary 정의하고 두 업종에 불러 보기
import pandas as pd

pd.set_option("display.unicode.east_asian_width", True)
pd.set_option("display.float_format", "{:,.1f}".format)
FILE = "../data/상장사_재무_2021_2025.xlsx"

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


print(summary("의약품 제조업").to_string(index=False))
print(summary("반도체 제조업").to_string(index=False))
