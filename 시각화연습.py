import pandas as pd
import matplotlib.pyplot as plt

데이터 = {
    '월' : ["1월", "2월", "3월", "4월", "5월"],
    "싼거" : [50, 65, 45, 70, 55],
    "기본" : [80, 85, 90, 105, 110],
    "비싼거" : [20, 35, 40, 60, 85]
}

표 = pd.DataFrame(데이터)

plt.rc('font', family = 'Malgun Gothic')

plt.figure(figsize = (10, 6))
plt.plot(표['월'], 표['싼거'], marker = 'o', label = "싼거(찬물)", color = '#42a5f5', linewidth = 2)
plt.plot(표['월'], 표['기본'], marker = 's', label = "기본(찬물+더운물)", color = '#ffb74d', linewidth = 2)
plt.plot(표['월'], 표['비싼거'], marker = '^', label = "비싼거(얼음)", color = '#ef5350', linewidth = 2)

plt.title("정수기 공장 등급별 월간 판매 현황", fontsize = 16, fontweight = 'bold', pad = 20)
plt.xlabel("판매 월", fontsize = 12)
plt.ylabel("판매량 (대)", fontsize = 12)
plt.legend(fontsize = 11)

plt.show()