# pandas로 저장한 엑셀: 값은 들어가지만 서식은 정할 수 없음
import pandas as pd

pd.set_option("display.unicode.east_asian_width", True)
FILE = "../data/상장사_재무_2021_2025.xlsx"
df = pd.read_excel(FILE, sheet_name="2025", dtype={"종목코드": str})
info = pd.read_excel(FILE, sheet_name="회사정보", dtype={"종목코드": str})
df25 = df.merge(info[["종목코드", "시장", "업종"]], on="종목코드", how="left")

ph = df25[df25["업종"] == "의약품 제조업"].copy()
ph["매출액(억 원)"] = ph["매출액"] / 100
ph["영업이익(억 원)"] = ph["영업이익"] / 100
ph["영업이익률"] = ph["영업이익"] / ph["매출액"].where(ph["매출액"] > 0)
cols = ["회사명", "시장", "매출액(억 원)", "영업이익(억 원)", "영업이익률"]
table = ph.sort_values("매출액", ascending=False)[cols]
print(table.head(3))

with pd.ExcelWriter("../내작업/p12_pandas저장.xlsx") as writer:
    table.to_excel(writer, sheet_name="회사별", index=False)
print("저장 완료", table.shape)
