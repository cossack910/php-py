n = int(input())

tree_dict = {}
root_node = set([i for i in range(n)])

for i in range(n):
    tmp = list(map(int, input().split(' ')))
    idx, children = tmp[0], tmp[1:]
    tree_dict[idx] = children
    root_node = root_node.difference(set(children))

root_idx = list(root_node)[0]
root_degree = 2
if tree_dict[root_idx].count(-1) == 2: root_degree = 0
if tree_dict[root_idx].count(-1) == 1: root_degree = 1

point = [[root_idx, -1, -1, root_degree, 0, 0]] #idx, parent, sibling, degree, depth, heigth
ans = {}

while point:
    idx, parent, sibling, degree, depth, height = point.pop()

    if parent == -1:
        ans[idx] = [parent , sibling, degree, depth, height, 'root']   
    elif tree_dict[idx][0] == -1 and tree_dict[idx][1] == -1:
        height = 0
        ans[idx] = [parent, sibling, 0, depth, height, 'leaf']
        parent_idx = parent
        while parent_idx != -1: #heigthを葉から求める
            height += 1
            if ans[parent_idx][4] < height:
                ans[parent_idx][4] = height
            parent_idx = ans[parent_idx][0]
    else:
        ans[idx] = [parent, sibling, degree, depth, height, 'internal node']

    for child_idx in tree_dict[idx]:
        if child_idx != -1:
            i = 0 
            if tree_dict[idx].index(child_idx) == 0: i = 1
            point.append([child_idx, idx, tree_dict[idx][i], 2 - tree_dict[child_idx].count(-1), depth + 1, height - 1]) #idx, parent, sibling, degree, depth, heigth

for i in range(n):
    print(f'node {str(i)}: parent = {str(ans[i][0])}, sibling = {str(ans[i][1])}, degree = {str(ans[i][2])}, depth = {str(ans[i][3])}, height = {str(ans[i][4])}, {ans[i][5]}')