dwarfs = [int(input()) for _ in range(9)]
total_height = sum(dwarfs)
target = total_height - 100

# 두 난쟁이를 찾기
for i in range(9):
    for j in range(i + 1, 9):
        if dwarfs[i] + dwarfs[j] == target:
            fake_dwarf1 = dwarfs[i]
            fake_dwarf2 = dwarfs[j]
            break

# 두 난쟁이를 제외하고 나머지 일곱 난쟁이를 찾기
real_dwarfs = [dwarf for dwarf in dwarfs if dwarf != fake_dwarf1 and dwarf != fake_dwarf2]

# 오름차순으로 정렬
real_dwarfs.sort()

# 결과 출력
for dwarf in real_dwarfs:
    print(dwarf)