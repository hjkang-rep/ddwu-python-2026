# 0으로 나누기와 빈칸: 파이썬 숫자와 pandas 열의 차이
import numpy as np
import pandas as pd

idx = ["가", "나", "다", "라", "마"]
top = pd.Series([10.0, -10.0, 0.0, 5.0, np.nan], index=idx)
bottom = pd.Series([0.0, 0.0, 0.0, np.nan, 5.0], index=idx)
r = top / bottom
print(pd.DataFrame({"분자": top, "분모": bottom, "결과": r}))
print(r.isna().sum(), np.isinf(r).sum())   # NaN 개수, inf 개수
print(r.max(), r.min())                     # inf가 섞이면 최댓값 · 최솟값이 inf
try:
    print(10 / 0)                           # 파이썬 숫자끼리는 오류
except ZeroDivisionError as e:
    print("ZeroDivisionError:", e)
