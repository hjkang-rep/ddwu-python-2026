# 쉼표만 없애고 숫자로 바꾸면 '-' 한 글자에서 멈춤
import pandas as pd

FILE = "../data/상장사_재무_원자료_2025.xlsx"
raw = pd.read_excel(FILE, sheet_name="원자료", dtype=str)

txt = raw["thstrm_amount"].str.replace(",", "", regex=False)
print(txt.head(3).tolist())
num = pd.to_numeric(txt)      # 여기서 ValueError
print(num.head(3))
