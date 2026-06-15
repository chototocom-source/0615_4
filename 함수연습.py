def basic_purifier():
    print("정수기 필터 통과하는중...")
    return "시원한 찬물만 있습니다."

# 실행식
my_drink = basic_purifier()
print(f"결과: {my_drink}")


def 냉온수정수기(선택):
    print("정수기 필터를 통과하는 중...")

    if 선택 == "찬물":
        return "시원한 찬물 한 잔"
    elif 선택 == "더운물":
        return "따뜻한 더운물 한 잔"
    else:
        return "X"
    
my_drink = 냉온수정수기("더운물")
print(f"결과: {my_drink}")

def 냉온수정수기(선택 = "찬물"):
    if 선택 == "찬물":
        return "시원한 찬물 한 잔"
    elif 선택 == "더운물":
        return "따뜻한 더운물 한 잔"
    else:
        return "X"
    
my_drink = 냉온수정수기()
print(f"결과: {my_drink}")

import datetime as dt

print(f"datetime 핵심기능 보여줘: {dir(dt)}")