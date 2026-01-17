# toy_word_count

텍스트(txt)파일을 입력으로 받아 단어 빈도를 계산하고, 가장 많이 등장한 단어 TOP N을 출력하는 간단한 파이썬 토이 프로젝트 입니다.

# Features

1. txt 파일 읽기
2. 대소문자 구분 없이 단어 처리
3. 단어 빈도 계산
4. 빈도 기준 TOP N 단어 출력

# Tech Stack

1. python3
2. Standard Library(os)

# Project Structure

toy_word_count/
  - word_count.py
  - sample.txt

# How to Run

python word_count.py

# Example Output

Frequency of words TOP 5
hello : 5
world : 3
python : 2

# Notes

1. 파일 경로 문제를 해결하기 위해 현재 파일 위치 기준으로 txt파일을 읽도록 구현했습니다.
2. Git과 Github 사용 연습을 위한 토이 프로젝트입니다.