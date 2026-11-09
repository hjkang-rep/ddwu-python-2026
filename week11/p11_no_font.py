# 한글 폰트를 설정하지 않으면: 글자가 네모로 나오고 경고가 뜸
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(4.8, 3))
ax.plot(["2021", "2022", "2023"], [279.6, 302.2, 258.9], marker="o", color="#2a78d6")
ax.set_title("삼성전자 매출액")
ax.set_ylabel("조 원")
plt.savefig("../내작업/p11_폰트없음.png", dpi=150, bbox_inches="tight")
plt.show()                                     # 실행 단추로 돌리면 창이 뜨지 않음
print("저장 완료")
