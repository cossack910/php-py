n = int(input())

dict = {}
for i in range(n):
    val = input()
    if ' ' in val:
        do, number = val.split(' ')
        
        if do == 'insert':
            dict.update({number : "x"})
        
        if do == 'delete':
            dict.pop(number, None)
    else:
        if val == 'deleteFirst':
            for key in list(dict.keys()):
                dict.pop(key)
                break
            
        if val == 'deleteLast':
            dict.popitem()
            
print(' '.join([i for i in dict.keys()]))