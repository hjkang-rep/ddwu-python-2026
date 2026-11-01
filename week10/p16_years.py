# 연도 시트 다섯 개를 반복문으로: 반도체 제조업 매출 합계
import pandas as pd

# 모든 시트의 종목코드를 문자열로 읽음
books = pd.read_excel("../data/상장사_재무_2021_2025.xlsx",
                      sheet_name=None,
                      dtype={"종목코드": str})
info = books["회사정보"]
semi = info[info["업종"] == "반도체 제조업"]["종목코드"]
for year in ["2021", "2022", "2023", "2024", "2025"]:
    d = books[year]
    s = d[d["종목코드"].isin(semi)]
    print(year, len(s), round(s["매출액"].sum() / 1_000_000, 1))
