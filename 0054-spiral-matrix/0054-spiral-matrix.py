class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res=[]
        while matrix:
            #take 1st row
            res.extend(matrix.pop(0))

            #take last column
            if matrix:
                for row in matrix:
                    res.append(row.pop(-1))
                while matrix and not matrix[0]:
                    matrix.pop(0)
            #take last row reverse
            if matrix:
                res.extend(matrix.pop()[::-1])

            #take 1st column reversed
            if matrix:
                print('deb\n', matrix)
                for row in range (-1,-(len(matrix)+1),-1):
                    res.append(matrix[row].pop(0))
                while matrix and not matrix[-1]:
                    matrix.pop()                    
        return res
# S.C=O(n), T.C=O(n)