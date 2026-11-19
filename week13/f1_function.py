# 1단계: 업종 상위 5개 표를 만드는 함수 top5 정의하고 한 번 부르기 (2025년, 금액 단위는 백만 원)
import pandas as pd

pd.set_option("display.unicode.east_asian_width", True)
pd.set_option("display.float_format", "{:,.1f}".format)   # 숫자를 쉼표 · 소수 한 자리로 보여 줌
FILE = "../data/상장사_재무_2021_2025.xlsx"

# 준비: 함수가 쓸 표 ok 를 먼저 만듦 (영업이익률을 계산하고, 이상한 행을 거르고, 업종을 붙임)
df = pd.read_excel(FILE, sheet_name="2025", dtype={"종목코드": str})
info = pd.read_excel(FILE, sheet_name="회사정보", dtype={"종목코드": str})
df["영업이익률"] = df["영업이익"] / df["매출액"] * 100
ok = df[(df["매출액"] > 0) & df["영업이익"].notna()]
ok = ok.merge(info[["종목코드", "업종"]], on="종목코드")


def top5(industry):
    """업종 이름을 받아 영업이익률 상위 5개 회사 표를 돌려줌"""
    mine = ok[ok["업종"] == industry]
    top = mine.sort_values("영업이익률", ascending=False).head(5)
    return top[["회사명", "매출액", "영업이익", "영업이익률"]].round(1)


t = top5("의약품 제조업")      # 함수 부르기: 돌려준 표를 t 에 담음
print(t.to_string(index=False))
