'''[1 2 3 
4 5 6
7 8 9 ]'''
#output = [1,2,3,6,9,8,7,4,5]
matrix = [[1,2,3],[4,5,6],[7,8,9]]
output = []
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if i%2==0:
            output.append(matrix[i][j])
        else :
            output.append(matrix[i][len(matrix[i])-1-j])


        
        
print(output)

