from pathlib import Path # cf) from pathlib import * -> pathlib에서 모든거 다 가져오기
import pandas as pd

data = {
    '이름' : ['김우주', '이민우', '박서연'],
    '나이' : [25, 34, 29],
    '직업' : ['개발자', '디자이너', '강사']
}

df = pd.DataFrame(data)

# 1. 만들고 싶은 폴더와 파일명을 한 번에 적어줍니다.
file_path = Path("data/output_file.csv")

# 2. 폴더가 없으면 만들어라! (이거 한 줄이면 끝납니다)
file_path.parent.mkdir(parents=True, exist_ok=True) # mkdir -> make directory

# 3. 그대로 저장
df.to_csv(file_path, index=False, encoding="utf-8-sig")