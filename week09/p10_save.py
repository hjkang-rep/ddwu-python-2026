# 결과를 엑셀로 저장: 보고표 한 장
import pandas as pd
pd.set_option("display.unicode.east_asian_width", True)  # 한글이 섞인 표의 열을 맞춤

df = pd.read_excel("매출대장_9월.xlsx", header=2)
done = df[df["상태"] == "완료"]
report = done.groupby("분류")["금액"].sum().reset_index()
print(report)
report.to_excel("분류별_매출.xlsx", index=False)
print("저장 완료")
