# def abc(level):
#     print(1)
#     if level==2:
#         print(2)
#         return
#     print(3)
#     abc(level+1)
#     print(4)
#
# abc(0)




def abc(level):
    print('1', end='')
    if level==2:
        # print('2', end='')
        return
    # print('3', end='')
    for i in range(2):
        # print('4', end='')
        abc(level+1)
        # print('5', end='')
    # print('6', end='')

abc(0)