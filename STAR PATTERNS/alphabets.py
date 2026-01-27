for i in range(4,0,-1):
    print("*".join(chr(j) for j in range(65,65+i)))
'''
A*B*C*D
A*B*C
A*B
A'''

# increasing 
for i in range(1,5):
    print("*".join(chr(j) for j in range(65,65+i)))
    '''
A
A*B
A*B*C
A*B*C*D'''


# lower case 
for i in range(4,0,-1):
    print("*".join(chr(j) for j in range(97,97+i)))
'''
a*b*c*d
a*b*c
a*b
a
'''

# numbers
for i in range(5,0,-1):
    print("*".join(str(j) for j in range(1,i+1)))
'''
1
1*2
1*2*3
1*2*3*4'''







 
