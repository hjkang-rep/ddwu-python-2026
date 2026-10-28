# 따라 하기: 매출 대장에서 지점별 보고표까지 (읽기 -> 정리 -> 거르기 -> 집계 -> 저장)
import pandas as pd
pd.set_option("display.unicode.east_asian_width", True)  # 한글이 섞인 표의 열을 맞춤

# 1. 읽기: 제목 두 줄을 건너뜀
df = pd.read_excel("매출대장_9월.xlsx", header=2)

# 2. 정리: 합계 줄을 지우고, 지점 이름의 앞뒤 빈칸을 없앰
df = df[df["지점"] != "합계"].copy()
df["지점"] = df["지점"].str.strip()
print(df.shape, list(df["지점"].unique()))

# 3. 거르기: 완료 주문만
done = df[df["상태"] == "완료"]

# 4. 집계: 지점마다 주문 수 · 매출 · 객단가
report = done.groupby("지점").agg(주문수=("주문번호", "count"), 매출=("금액", "sum"))
report["객단가"] = (report["매출"] / report["주문수"]).round()
report = report.sort_values("매출", ascending=False)
print(report)

# 5. 저장
report.to_excel("지점별_보고표.xlsx")
print("저장 완료")
