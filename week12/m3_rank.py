# 3단계: 내 업종의 영업이익률 상위 5개 회사를 엑셀로 저장
import pandas as pd

pd.set_option("display.unicode.east_asian_width", True)
pd.set_option("display.float_format", "{:,.1f}".format)   # 숫자를 쉼표 · 소수 한 자리로 보여 줌
FILE = "../data/상장사_재무_2021_2025.xlsx"
INDUSTRY = "의약품 제조업"   # 여기만 바꿈. 정확한 이름은 find_industry.py로 찾음

df = pd.read_excel(FILE, sheet_name="2025", dtype={"종목코드": str})
info = pd.read_excel(FILE, sheet_name="회사정보", dtype={"종목코드": str})

df["영업이익률"] = df["영업이익"] / df["매출액"] * 100
ok = df[(df["매출액"] > 0) & df["영업이익"].notna()]
ok = ok.merge(info[["종목코드", "업종"]], on="종목코드")   # 회사정보 시트의 업종 열을 붙임

mine = ok[ok["업종"] == INDUSTRY]
print(INDUSTRY, len(mine), "곳")
if len(mine) == 0:
    print("0곳: 업종 이름이 파일과 다르거나(find_industry.py로 확인), 은행 · 보험처럼 영업이익 칸이 빈 업종")

top5 = mine.sort_values("영업이익률", ascending=False).head(5)
top5 = top5[["회사명", "매출액", "영업이익", "영업이익률"]].round(1)
print(top5.to_string(index=False))

top5.to_excel("../내작업/w12_내업종.xlsx", index=False)
print("저장 완료: 내작업/w12_내업종.xlsx")
