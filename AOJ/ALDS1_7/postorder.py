# C問題の先行巡回
n = int(input())

ans = []
root_node = set([i for i in range(n)])

def postorder(idx):
    # 再帰の終了条件（ノードが-1(ノードなし)
    if idx == -1:
        return
    # 左部分木の処理
    postorder(nodes[idx]["left"])
    # 右部分木の処理
    postorder(nodes[idx]["right"])
    # 節点の処理
    ans.append(idx)
    
nodes = {}
for _ in range(n):
    tmp = list(map(int, input().split(' ')))
    idx, left, right = tmp[0], tmp[1], tmp[2]
    nodes[idx] = { "left" : left, "right" : right }
    root_node = root_node - set([left, right])
    
root_idx = list(root_node)[0]
postorder(root_idx)
print(ans)