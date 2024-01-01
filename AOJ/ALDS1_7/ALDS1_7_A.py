n = int(input())

tree_dict = {} 
children_set = set([i for i in range(n)])

for i in range(n):
    A = list(map(int, input().split(' ')))
    idx,k,children = A[0],A[1],A[2:]
    tree_dict[idx] = children
    children_set = children_set - set(children)#木全体から子を差集合していくことでroot(根)が求められる

node_info = [[list(children_set)[0],-1,0]]# idx, 親, 深さ　探索のスタート地点なので必ず親と深さは-1, 0で固定
anser_dict = {}

while node_info:
    idx, parent, depth = node_info.pop()
    if parent == -1:
        anser_dict[idx] = [idx,parent,depth,"root",tree_dict[idx]]
    elif len(tree_dict[idx]) > 0:
        anser_dict[idx] = [idx,parent,depth,"internal node",tree_dict[idx]]
    else:
        anser_dict[idx] = [idx,parent,depth,"leaf",tree_dict[idx]]
        
    for child in tree_dict[idx]:
        node_info.append([child,idx,depth+1])

for i in range(n):
    print(f"node {i}: parent = {anser_dict[i][1]}, depth = {anser_dict[i][2]}, {anser_dict[i][3]}, {anser_dict[i][4]}")
