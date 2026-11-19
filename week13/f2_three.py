# 2단계: 함수 top5 를 반복문으로 세 번 불러, 시트 세 장짜리 엑셀 파일 하나로 저장
import pandas as pd

pd.set_option("display.unicode.east_asian_width", True)
pd.set_option("display.float_format", "{:,.1f}".format)
FILE = "../data/상장사_재무_2021_2025.xlsx"

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


INDUSTRIES = ["의약품 제조업", "기타 화학제품 제조업", "반도체 제조업"]   # 여기만 바꿈

writer = pd.ExcelWriter("../내작업/w13_세업종.xlsx")    # 엑셀 파일 하나를 엶
for name in INDUSTRIES:
    t = top5(name)
    print(name, "1위:", t.iloc[0]["회사명"], t.iloc[0]["영업이익률"])
    t.to_excel(writer, sheet_name=name[:31], index=False)   # 시트 이름은 31자까지
writer.close()                                           # 닫아야 파일이 완성됨
print("저장 완료: 내작업/w13_세업종.xlsx")
