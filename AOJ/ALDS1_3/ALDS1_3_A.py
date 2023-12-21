operators = ['+', '-', '*']
inputs = input().split(' ')

stacks = []
for i in inputs:
    if i not in operators:
        stacks.append(int(i))
        continue
    
    if i == operators[0]:
        stacks.append(stacks.pop()+stacks.pop())
    
    if i == operators[2]:
        stacks.append(stacks.pop()*stacks.pop())
        
    if i == operators[1]:
        stacks.append(stacks.pop(-2)-stacks.pop())
        
print(stacks[0])