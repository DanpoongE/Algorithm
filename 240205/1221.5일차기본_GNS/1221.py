T = int(input())

for _ in range(1, T+1):
    hash_number, N = list(map(str, input().split()))
    arr = list(map(str, input().split()))

    dict = {'ZRO':0, 'ONE':1, 'TWO':2, 'THR':3, 'FOR':4, 'FIV':5, 'SIX':6, 'SVN':7, 'EGT':8, 'NIN':9}
    rev_dict = {0:'ZRO', 1:'ONE', 2:'TWO', 3:'THR', 4:'FOR', 5:'FIV', 6:'SIX', 7:'SVN', 8:'EGT', 9:'NIN'}
    empty_list = []
    result_list = []

    for words in arr:
        empty_list.append(dict[words])

    empty_list.sort()

    for nums in empty_list:
        result_list.append(rev_dict[nums])

    print(hash_number)
    print(*result_list)