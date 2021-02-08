# Chapter09-02
# CSV 파일 읽기 및 쓰기

# CSV : MEME - text/csv

import csv

# ex1
with open('./resource/test1.csv', 'r') as f:
    reader = csv.reader(f)
