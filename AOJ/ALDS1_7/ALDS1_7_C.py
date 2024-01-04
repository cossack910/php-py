n = int(input())

tree_dict = {}
root_node = set([i for i in range(n)])
for _ in range(n):
    tmp = list(map(int, input().split(' ')))
    idx, left, right = tmp[0], tmp[1], tmp[2]
    tree_dict[idx] = { "left" : left, "right" : right }
    root_node = root_node - set([left, right])

preoder = []
root_node = list(root_node)[0]
pre_point = [root_node]
while pre_point:
    idx = pre_point.pop()
    preoder.append(idx)
    #右から先入、左から後出しすることで左分岐優先となる
    if tree_dict[idx]["right"] != -1:
        pre_point.append(tree_dict[idx]["right"])
    if tree_dict[idx]["left"] != -1:
        pre_point.append(tree_dict[idx]["left"])
print("Preorder")
print(' ' + ' '.join(list(map(str, preoder))))

inorder = []
def searchLeftNode(node, n):
    for _ in range(n):
        if node == root_node and tree_dict[node]["left"] == -1:
            break
        if tree_dict[node]["left"] == -1:
            break
        if tree_dict[node]["left"] != -1:
            node = tree_dict[node]["left"]
    return node

def parentCheck(idx, n, root_node):
    if idx == root_node:
        return -1      
    for i in range(n):
        if idx in tree_dict[i].values():
            return i
        
in_start_node = searchLeftNode(root_node, n)
in_point = [[in_start_node, tree_dict[in_start_node], parentCheck(in_start_node, n, root_node)]]

while in_point:
    idx, children, parent = in_point.pop()
    if parent == -1 and idx in inorder:
        break
    if parent == -1:
        inorder.append(idx)
        if children["right"] != -1:
            a = searchLeftNode(children["right"], n)
            in_point.append([a, tree_dict[a], parentCheck(a, n, root_node)])
            continue
        else:
            break
    
    left_node = searchLeftNode(idx, n)
    if left_node != idx and left_node not in inorder:
        in_point.append([left_node, tree_dict[left_node], parentCheck(left_node, n, root_node)])
        continue
    
    if left_node != idx and left_node in inorder:
        in_point.append([left_node, tree_dict[left_node], parentCheck(left_node, n, root_node)])
        
    if left_node != idx and tree_dict[idx]["right"] != -1  and left_node in inorder:
        next_left_node = searchLeftNode(tree_dict[idx]["right"], n)
        in_point.append([next_left_node, tree_dict[next_left_node], parentCheck(next_left_node, n, root_node)])
        
    if left_node == idx and tree_dict[idx]["right"] != -1 and tree_dict[idx]["right"] not in inorder:
        in_point.append([tree_dict[idx]["right"], tree_dict[tree_dict[idx]["right"]], idx])

    if left_node == idx and tree_dict[idx]["left"] == -1 and tree_dict[idx]["right"] == -1:
        parent = parentCheck(left_node, n , root_node)
        in_point.append([parent, tree_dict[parent], parentCheck(parent, n, root_node)])
    
    if idx in inorder:
        parent = parentCheck(idx, n , root_node)
        in_point.append([parent, tree_dict[parent], parentCheck(parent, n, root_node)])
        
    if idx not in inorder:
        inorder.append(idx)

print("Inorder")
print(' ' + ' '.join(list(map(str, inorder))))

def searchPostNode(node, n):
    for _ in range(n):
        if tree_dict[node]["left"] == -1 and tree_dict[node]["right"] == -1:
            break
        if tree_dict[node]["left"] != -1:
            node = tree_dict[node]["left"]  
        if tree_dict[node]["left"] == -1 and tree_dict[node]["right"] != -1:
            node = tree_dict[node]["right"]
    return node

post_start_node = searchPostNode(root_node, n)
post_point = [[post_start_node, tree_dict[post_start_node], parentCheck(post_start_node, n, root_node)]]

postorder = []
while post_point:
    idx, children, parent = post_point.pop()
    
    if parent == -1 and tree_dict[idx]["left"] != -1 and tree_dict[idx]["right"] != -1:
        post_node = searchPostNode(tree_dict[idx]["right"], n)
        post_point.append([post_node, tree_dict[post_node], parentCheck(post_node, n, root_node)])
        if post_node in postorder:
            postorder.append(idx)
            break
    elif parent == -1 and (tree_dict[idx]["left"] == -1 or tree_dict[idx]["right"] == -1):
        postorder.append(idx)
        break
    
    post_node = searchPostNode(idx, n)
    if post_node != idx and tree_dict[idx]["right"] != -1 and tree_dict[idx]["right"] not in postorder:
        next_post_node = searchPostNode(tree_dict[idx]["right"], n)
        post_point.append([next_post_node, tree_dict[next_post_node], parentCheck(next_post_node, n, root_node)])
        continue
    
    if post_node != idx and post_node in postorder:
        parent = parentCheck(idx, n, root_node)
        post_point.append([parent, tree_dict[parent], parentCheck(parent, n, root_node)])

    if post_node == idx and tree_dict[idx]["left"] == -1 and tree_dict[idx]["right"] == -1:
        parent = parentCheck(post_node, n, root_node)
        post_point.append([parent, tree_dict[parent], parentCheck(parent, n, root_node)])    
           
    if idx not in postorder:
        postorder.append(idx)

print("Postorder")
print(' ' + ' '.join(list(map(str, postorder))))
