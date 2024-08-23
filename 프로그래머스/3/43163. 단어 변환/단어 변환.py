from collections import deque

def is_one_letter_diff(word1, word2):# 두 단어가 한 글자만 다른지 확인하는 함수
    diff_count = sum(a != b for a, b in zip(word1, word2))
    return diff_count == 1

def solution(begin, target, words):
    if target not in words:
        return 0
    
    words = set(words)  # 집합으로 변환하여 중복 방지 및 빠른 검색
    queue = deque([(begin, 0)])  # (현재 단어, 단계 수)
    visited = set([begin])
    
    while queue:
        current_word, steps = queue.popleft()
        
        if current_word == target:
            return steps
        
        for word in words:
            if word not in visited and is_one_letter_diff(current_word, word):
                visited.add(word)
                queue.append((word, steps + 1))
    
    return 0