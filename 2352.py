'''
Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) such that row ri and column cj are equal.

A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).
'''
class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        pairs = 0
        rows = defaultdict(int)

        for row in grid:
            rows[tuple(row)] += 1
        for col in range(n):
            column = tuple(grid[r][col] for r in range(n))
            if column in rows:
                pairs += rows[column]
        return pairs

# time complexity is O(n^2)
# space complexity is O(n^2)
