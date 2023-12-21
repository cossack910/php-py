n, q = map(int, input().split(' '))

current_time = 0
queue = {}
ansers = {}
for i in range(n):
    name, time = input().split(' ')
    time = int(time)
    
    if time > q:
        queue.update({name : time - q})
        current_time += q
        continue
    
    if time <= q:
        current_time += time
        ansers.update({name : current_time})

while len(queue) > 0:
    for key in list(queue.keys()):
        if queue[key] > q:
            queue.update({ key : queue[key] - q})
            current_time += q
            continue
        
        if queue[key] <= q:
            current_time += queue[key]
            ansers.update({ key : current_time })
            queue.pop(key)

for key, value in ansers.items():
    print(key, value)