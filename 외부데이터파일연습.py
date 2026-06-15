from pathlib import Path
import pandas as pd

data = {
    '이름' : ['김우주', '이민우', '박서연'],
    '나이' : [25, 34, 29],
    '직업' : ['개발자', '디자이너', '강사']
}

df = pd.DataFrame(data)

file_path = Path("data/output_file2.csv")

file_path.parent.mkdir(parents = True, exist_ok = True)

df.to_csv(file_path, index = True, encoding = 'utf-8-sig')