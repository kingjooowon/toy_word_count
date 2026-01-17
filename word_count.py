import os
import string

# 1. 이 파일이 있는 폴더를 기준으로 sample.txt 찾기
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(BASE_DIR, "sample.txt")

# 2. 파일 읽기
with open(file_path, "r", encoding="utf-8") as f:
    text = f.read()
    
words = text.lower().split()

word_count = {}

for word in words:
    word = word.strip(string.punctuation)
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
        
sorted_words = sorted(
    word_count.items(),
    key=lambda x: x[1],
    reverse = True
)

print("Frequency of words TOP 5")
for word, count in sorted_words[:5]:
    print(word, ":", count)