n = int(input())
preorder = list(map(int, input().split(' ')))
inorder = list(map(int, input().split(' ')))

root_node = preorder[0]

inorder_root_idx = inorder.index(root_node)
left_tree = inorder[:inorder_root_idx]
right_tree = inorder[inorder_root_idx + 1:]
print(left_tree)
print(right_tree)