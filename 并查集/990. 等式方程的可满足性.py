# https://leetcode-cn.com/problems/satisfiability-of-equality-equations/
# 并查集，先对等号进行union，再对不等号找根节点判断是否相同

class Solution:

    class UnionFind:
        def __init__(self):
            self.parent = list(range(26))
        
        def find(self, index):
            if index == self.parent[index]:
                return index
            self.parent[index] = self.find(self.parent[index])
            return self.parent[index]
        
        def union(self, index1, index2):
            self.parent[self.find(index1)] = self.find(index2)


    def equationsPossible(self, equations: List[str]) -> bool:
        uf = Solution.UnionFind()
        for st in equations:
            if st[1] == "=":
                index1 = ord(st[0]) - ord("a")
                index2 = ord(st[3]) - ord("a")
                uf.union(index1, index2)
        for st in equations:
            if st[1] == "!":
                index1 = ord(st[0]) - ord("a")
                index2 = ord(st[3]) - ord("a")
                if uf.find(index1) == uf.find(index2):
                    return False
        return True
