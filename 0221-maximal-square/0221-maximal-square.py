class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows,cols=len(matrix),len(matrix[0])
        memo={}
        def maxLength(r,c):
            if r>=rows or c>=cols:
                return 0
            if (r,c) not in memo:
                memo[(r,c)]=0
                right=maxLength(r+1,c)
                down=maxLength(r,c+1)
                diag=maxLength(r+1,c+1)
                if matrix[r][c]=='1':
                    memo[(r,c)]=1+min(right,down,diag)
                    
            return memo[(r,c)]
        maxLength(0,0)
        return max(memo.values())**2
