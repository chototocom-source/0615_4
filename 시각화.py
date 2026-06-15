import pandas as pd
import matplotlib.pyplot as plt  # pip install pandas matplotlib -> terminal에 입력 필요

# 1. 1월부터 5월까지의 정수기 등급별 판매량 데이터 생성: key-(행, 가로), value-(열, 세로)
데이터 = {
    "월": ["1월", "2월", "3월", "4월", "5월"],
    "싼거": [50, 65, 45, 70, 55],
    "기본": [80, 85, 90, 105, 110],
    "비싼거": [20, 35, 40, 60, 85]
}


# 2. 딕셔너리 데이터를 판다스의 DataFrame(표 형태)으로 변환
표 = pd.DataFrame(데이터)

print("=== 판다스가 조립한 최종 데이터프레임 표 ===")
print(표)

# 상위 3개만 보기
print(표.head(3), '\n')

# 하위 3개만 보기
print(표.tail(3))

# 데이터프레임의 전체 요약 정보 출력 -> null값 확인
표.info()

# '1월' 행의 데이터만 이름으로 가져오기: loc[x번째 줄]
print(f"\n 첫 줄 노즐 \n\n {표.loc[0]}")
# 열 단위로 보기: def['값']
print(f"\n 싼거 데이터열 노출 \n\n {표['싼거']}")
# 행, 열 가져올 시에는: iloc[x번째 줄, y번째 칸] -> 값으로 나옴
print(f"\n 첫 줄의 첫번째 칸 값은? \n\n {표.iloc[0, 0]}")


# 3. 데이터 시각화 (그래프 그리기) 설정 -> 필수!!
# 한글 폰트 깨짐 방지 (윈도우 기준 맑은 고딕 설정) -> rc 함수는 '기본 스타일 환경 설정'을 통째로 제어(Control)하는 기능
plt.rc('font', family='Malgun Gothic')

# 그래프 크기 설정 및 선 그래프 그리기
plt.figure(figsize=(10, 6)) # 그래프의 가로, 세로 비율 -> 10 : 6
plt.plot(표["월"], 표["싼거"], marker='o', label="싼거 (찬물)", color='#42a5f5', linewidth=2) # x("월"), y("싼거")축 설정 -> 순서 중요! , # marker: 좌표 무늬 설정 , # linewidth = 줄 굴기
plt.plot(표["월"], 표["기본"], marker='s', label="기본 (찬물+더운물)", color='#ffb74d', linewidth=2)
plt.plot(표["월"], 표["비싼거"], marker='^', label="비싼거 (얼음추가)", color='#ef5350', linewidth=2)


# 4. 그래프 꾸미기 (제목, 축 이름, 범례)
plt.title("📈 정수기 공장 등급별 월간 판매 현황", fontsize=16, fontweight='bold', pad=15)
plt.xlabel("판매 월", fontsize=12) # x축 라벨
plt.ylabel("판매량 (대)", fontsize=12) # y축 라벨
plt.grid(True, linestyle='--', alpha=0.6) # 배경 격자무늬
plt.legend(fontsize=11) # 범례 표시


# 5. 그래프 화면에 띄우기
plt.show()