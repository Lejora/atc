# from collections import deque


# def check_can_reach(board, start, stop):
#   rows, cols = len(board), len(board[0])
#   queue = deque([start])
#   visited = set([start])
  
#   directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
  
#   while queue:
#     r, c = queue.popleft()
    
#     if (r, c) == stop:
#       return True
    
#     for dr, dc in directions:
#       nr, nc = r + dr, c + dc
      
#       if 0 <= nr < rows and 0 <= nc < cols and \
#         board[nr][nc] == 1 and (nr, nc) not in visited:
#           visited.add((nr, nc))
#           queue.append((nr, nc))
    
#   return False
      
    
# def solve():
#   H, W = map(int, input().split())
#   Q = int(input())
  
#   board = [[0 for _ in range(W)] for _ in range(H)]
  
#   for _ in range(Q):
#     query = list(map(int, input().split()))
  
#     if query[0] == 1:
#       r = query[1] - 1
#       c = query[2] - 1
      
#       board[r][c] = 1
    
#     elif query[0] == 2:
#       ra = query[1] - 1 
#       ca = query[2] - 1
#       rb = query[3] - 1
#       cb = query[4] - 1
      
#       if board[ra][ca] == 0 or board[rb][cb] == 0:
#         print("No")
      
#       else:
#         if check_can_reach(board, (ra, ca), (rb, cb)):
#           print("Yes")
#         else:
#           print("No")
    
# solve()

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x):
        if self.parent[x] == x:
            return x
        # 経路圧縮（木を平たくして次回以降の検索を高速化）
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            # サイズが大きい方に小さい方をくっつける
            if self.size[root_x] < self.size[root_y]:
                root_x, root_y = root_y, root_x
            self.parent[root_y] = root_x
            self.size[root_x] += self.size[root_y]

    def same(self, x, y):
        return self.find(x) == self.find(y)


def solve():
    import sys
    # 入力量が多いので高速化
    input = sys.stdin.read
    data = input().split()
    
    if not data:
        return

    H = int(data[0])
    W = int(data[1])
    Q = int(data[2])
    
    # 2次元の座標 (r, c) を 1次元のインデックスに変換する関数
    def to_1d(r, c):
        return r * W + c

    uf = UnionFind(H * W)
    # 赤く塗られているかどうかのフラグ
    is_red = [[False] * W for _ in range(H)]
    
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    idx = 3
    
    for _ in range(Q):
        q_type = int(data[idx])
        
        if q_type == 1:
            r = int(data[idx+1]) - 1
            c = int(data[idx+2]) - 1
            idx += 3
            
            is_red[r][c] = True
            
            # 上下左右を見て、すでに赤いマスがあればUnion-Findで結合
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < H and 0 <= nc < W and is_red[nr][nc]:
                    uf.union(to_1d(r, c), to_1d(nr, nc))
                    
        elif q_type == 2:
            ra = int(data[idx+1]) - 1
            ca = int(data[idx+2]) - 1
            rb = int(data[idx+3]) - 1
            cb = int(data[idx+4]) - 1
            idx += 5
            
            # 両方のマスが赤色 かつ 同じグループに属しているか
            if is_red[ra][ca] and is_red[rb][cb] and uf.same(to_1d(ra, ca), to_1d(rb, cb)):
                print("Yes")
            else:
                print("No")

if __name__ == '__main__':
    solve()