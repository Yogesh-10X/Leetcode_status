class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        n=len(matrix)
        x=[[0]*n for z in range(len(matrix[0]))]
        for i in range(len(matrix[0])):
            for j in range(0,n):
                x[i][j]=matrix[j][i]
        return x
