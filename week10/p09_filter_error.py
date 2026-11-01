# 괄호가 빠진 조건식: & 가 비교보다 먼저 계산됨
import pandas as pd

df = pd.read_excel("../data/상장사_재무_2021_2025.xlsx", sheet_name="2025")
loss = df[df["매출액"] >= 1_000_000 & df["영업이익"] < 0]
