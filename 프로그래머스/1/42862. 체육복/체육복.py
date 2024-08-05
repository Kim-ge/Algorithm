def solution(n, lost, reserve):
    #여벌 체육복을 가진 학생이 도난당한 경우
    reserve_set = set(reserve) - set(lost)
    lost_set = set(lost) - set(reserve)
    
    #체육복을 빌려주는 과정
    for student in sorted(reserve_set):
        if student - 1 in lost_set:
            lost_set.remove(student - 1)
        elif student + 1 in lost_set:
            lost_set.remove(student + 1)
    
    #체육수업을 들을 수 있는 학생의 최댓값을 계산
    return n - len(lost_set)
