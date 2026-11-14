# matplotlib 그림을 PNG로 저장한 뒤 시트에 넣기 (pillow가 필요함)
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import font_manager
from openpyxl import load_workbook
from openpyxl.drawing.image import Image

font_manager.fontManager.addfont("../data/fonts/NanumGothic.ttf")
plt.rcParams["font.family"] = "NanumGothic"
plt.rcParams["axes.unicode_minus"] = False

OUT = "../내작업/p17_시트.xlsx"                     # p17을 먼저 실행해 둠
PNG = "../내작업/p18_추이.png"
trend = pd.read_excel(OUT, sheet_name="연도별 추이", index_col="연도")
print(trend["매출액"].round(0).tolist())

fig, ax = plt.subplots(figsize=(5, 3))
ax.bar(trend.index.astype(str), trend["매출액"] / 10_000, color="#2a78d6")   # 억 원 -> 조 원
ax.set_title("의약품 제조업 매출액 합계")
ax.set_xlabel("사업연도")
ax.set_ylabel("조 원")
plt.savefig(PNG, dpi=150, bbox_inches="tight")      # 1. 그림을 파일로
plt.close(fig)

wb = load_workbook(OUT)
ws = wb["연도별 추이"]
img = Image(PNG)                                     # 2. 파일을 그림 객체로
print(img.width, img.height)                         # 픽셀
img.width, img.height = img.width * 0.6, img.height * 0.6
ws.add_image(img, "H2")                              # 3. H2 칸에 왼쪽 위를 맞춤
wb.save("../내작업/p18_그림.xlsx")
print("저장 완료", len(ws._images))
