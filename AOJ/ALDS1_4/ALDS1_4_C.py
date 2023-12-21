from collections import deque

n = int(input())

dict = {}
for i in range(n):
    act, word = input().split(' ')
    if act == 'insert':
        dict.update({word : ''})
        continue
    
    if act == 'find' and word in dict:
        print('yes')
    else:
        print('no')