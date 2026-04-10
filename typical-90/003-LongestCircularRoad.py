from collections import deque


N = int(input())

# 各都市から行ける番号
G = [[] for _ in range(N+1)]

for i in range(N-1):
  A, B = map(int, input().split())
  
  G[A].append(B)
  G[B].append(A)
  
def get_distances(start_node, n, graph):
  distances = [-1] * (n + 1)
  
  distances[start_node] = 0
  queue = deque([start_node])
  
  while queue:
    current = queue.popleft()
    for next_city in graph[current]:
      if distances[next_city] == -1:
        distances[next_city] = distances[current] + 1
        queue.append(next_city)
        
  return distances

# この問題で求められているスコアは、新しく道を作ってできる「一番長いループ」の長さ
# 木の中で最も遠い2つの都市（距離を L とする）を選ぶ
# その2つの間に新しい道を1本引く　
# すると、もともとの道 L 本 ＋ 新しい道 1 本で、長さ L+1 のループが完成

# 適当な都市1から端を見つける
dist_from_1 = get_distances(1, N, G)
X = dist_from_1.index(max(dist_from_1))

# 端から一番遠いノードを見つける
dist_from_X = get_distances(X, N, G)
diameter = max(dist_from_X)

print(diameter + 1)