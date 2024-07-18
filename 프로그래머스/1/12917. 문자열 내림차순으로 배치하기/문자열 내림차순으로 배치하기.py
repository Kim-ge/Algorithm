def solution(s):
    sorted_str = sorted(s, reverse=True)
    return ''.join(sorted_str)