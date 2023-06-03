# # 9.105
# x = input('some word')
# if len(x) == 12:
#     print(x[0:3] + x[9:2:-1] + x[10:12])
# else:
#     print('error')


# # 9.90
# x = input('some word')
# xLen = len(x)
# v = xLen * (-1)
# while True:
#     if x[v] =='e':
#         print('i', end="")
#     else:
#         print(x[v], end="")
#     v += 1
#     xLen -= 1
#     if xLen == 0:
#         break


# # 9.92
# x = input('some text')
# xLen = len(x)
# c = xLen * (-1)
# v = 0
# while True:
#     v += 1
#     if v % 2 != 0:
#         print(x[c], end='')
#     elif v % 2 == 0:
#         print('ы', end='')
#     c += 1
#     xLen -= 1
#     if xLen == 0:
#         break


# # 9.38
# x = input('some word')
# z = input('symbol uslowiya')
# xLen = len(x)
# if xLen == 12:
#     if z == 'a':
#         print(x[4:8] + x[8:12] + x[:4])
#     elif z == 'b':
#         print(x[8:12] + x[0:4] + x[4:8])
#     else:
#         print('symbol on Englisch, a or b')
# else:
#     print('lenght word not 12 symbols')


# # 9.153
# x = input('input some text')
# symbol = input('iskomi symbol')
# xLen = len(x)
# z = (xLen * (-1))
# cnt = 0
# cnt1 = 0
# while True:
#     c = x[z]
#     if c == symbol:
#         cnt += 1
#     if cnt1 <= cnt:
#         cnt1 = cnt
#     if c != symbol:
#         cnt *= 0
#     z += 1
#     xLen -= 1
#     if z == 0:
#         break
# print(cnt1)