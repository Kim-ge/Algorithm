def solution(people, limit):
    people.sort()  #몸무게 오름차순 정렬
    left = 0       #가장 가벼운 사람을 가리키는 인덱스
    right = len(people) - 1  #가장 무거운 사람을 가리키는 인덱스
    boats = 0      #사용한 구명보트의 수

    while left <= right:
        #가장 가벼운 사람과 가장 무거운 사람이 함께 보트에 탈 수 있는지 확인
        if people[left] + people[right] <= limit:
            left += 1  #가벼운 사람을 보트에 태우고 인덱스를 오른쪽으로 이동
        #함께 탈 수 없는 경우 무거운 사람만 보트에 태우고 인덱스를 왼쪽으로 이동
        right -= 1
        #보트 추가
        boats += 1

    return boats