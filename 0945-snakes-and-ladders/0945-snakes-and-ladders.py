class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        visited=set()
        res=0
        rows,n=len(board),len(board)**2

        def mapNumCell(num:int):
            num-=1
            row=rows-1-num//rows
            if (rows-row)%2==1:
                col=num%rows
            else:
                col=rows-1-(num%rows)
            return (row,col)

        queue=deque([1])
        visited.add(1)

        while queue:
            for _ in range(len(queue)):
                i=queue.popleft()
                if i==n:
                    return res
                for d in range(1,7):
                    next_cell=i+d
                    if next_cell>n:
                        continue
                    r,c=mapNumCell(next_cell)
                    dest=board[r][c] if board[r][c]!=-1 else next_cell
                    if dest not in visited:
                        visited.add(dest)
                        queue.append(dest)
            res+=1

        return -1

