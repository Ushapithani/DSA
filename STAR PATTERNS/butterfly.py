'''
*        *
**      **
***    ***
****  ****
**********
****  ****
***    ***
**      **
*        *
'''
rows = 5

# Upper half
for i in range(1, rows+1):
    left = '*' * i
    space = ' ' * (2 * (rows - i))   
    right = '*' * i
    print(left + space + right)

# Lower half
for i in range(rows, 0, -1):
    left = '*' * i
    space = ' ' * (2 * (rows - i))
    right = '*' * i
    print(left + space + right)