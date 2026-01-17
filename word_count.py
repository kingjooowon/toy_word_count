import os
import sys
import string

def count_words(file_name, top_n):
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(BASE_DIR, file_name)
    
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()
        
    words = text.lower().split()
    
    word_count = {}
    for word in words:
        word = word.strip(string.punctuation)
        if not word:
            continue
        word_count[word] = word_count.get(word, 0) + 1
        
    sorted_words = sorted(
        word_count.items(),
        key=lambda x: x[1],
        reverse=True
    )
    
    return sorted_words[:top_n]

if __name__ == "__main__":
    file_name = sys.argv[1]
    top_n = int(sys.argv[2])
    
    result = count_words(file_name, top_n)
    
    print(f"Frequency of words TOP {top_n}")
    for word, count in result:
        print(word, ":", count)