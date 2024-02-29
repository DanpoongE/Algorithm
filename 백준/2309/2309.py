remove_idx = [] # 2개씩 끊어 읽기로 하자.
heights = []

# 제외할 난쟁이 번호 (0-8중 2개 숫자 조합)
def remove_num(level, start):
    if level == 2:
        r1, r2 = remove_idx
        if sum_val - heights[r1] - heights[r2] == 100:
            v1, v2 = heights[r1], heights[r2]
            heights.remove(v1)
            heights.remove(v2)
            heights.sort()
            print(*heights, sep='\n')
            return
        else:
            return

    for i in range(start, 9):
        remove_idx.append(i)
        remove_num(level + 1, i + 1)
        if len(heights) == 7:
            return
        remove_idx.pop()


for _ in range(9):
    height = int(input())
    heights.append(height)
# print(heights)

sum_val = sum(heights)
remove_num(0, 0)
