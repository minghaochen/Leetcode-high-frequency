# https://leetcode-cn.com/problems/number-of-islands/
# 深搜、广搜、并查集

class Solution:
    def dfs(self, grid, r, c):
        grid[r][c] = 0
        nr, nc = len(grid), len(grid[0])
        for x, y in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
            if 0 <= x < nr and 0 <= y < nc and grid[x][y] == "1":
                self.dfs(grid, x, y)

    def numIslands(self, grid: List[List[str]]) -> int:
        nr = len(grid)
        if nr == 0:
            return 0
        nc = len(grid[0])

        num_islands = 0
        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == "1":
                    num_islands += 1
                    self.dfs(grid, r, c)
        
        return num_islands

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        nr = len(grid)
        if nr == 0:
            return 0
        nc = len(grid[0])

        num_islands = 0
        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == "1":
                    num_islands += 1
                    grid[r][c] = "0"
                    neighbors = collections.deque([(r, c)])
                    while neighbors:
                        row, col = neighbors.popleft()
                        for x, y in [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]:
                            if 0 <= x < nr and 0 <= y < nc and grid[x][y] == "1":
                                neighbors.append((x, y))
                                grid[x][y] = "0"
        
        return num_islands

class UnionFind():
    def __init__(self,grid):
        m,n = len(grid), len(grid[0])
        self.parent = [-1]*(m*n) # 根节点数组
        self.rank = [0]*(m*n)
        self.count=0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    self.parent[i*n+j] = i*n+j
                    self.count+=1
    def find(self,x):
        if self.parent[x]==x:
            return x
        else:
            self.parent[x] = self.find(self.parent[x]) # 父节点设为根节点
            return self.parent[x] # 返回父节点
        return self.parent[x]
    def union(self,x,y):
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx != rooty:
            if self.rank[rootx] < self.rank[rooty]: # 按秩合并
                rootx, rooty = rooty, rootx
            self.parent[rooty] = rootx
            if self.rank[rootx] == self.rank[rooty]:
                self.rank[rootx] += 1
            self.count -= 1
    def getCount(self):
        return self.count

        

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m,n = len(grid), len(grid[0])
        uf = UnionFind(grid)
        num_islands = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == "1":
                    grid[r][c] = "0"
                    for x, y in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                        if 0 <= x < m and 0 <= y < n and grid[x][y] == "1":
                            uf.union(r * n + c, x * n + y)
        return uf.getCount()



