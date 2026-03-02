#input  = [10,36,45,3,2,1,12,20,50,16]
#output = [50,1,45,3,12,16,10,20,2,36]
input  = [10,36,45,3,2,1,12,20,50,16]
even_index = []
odd_index =[]
for i in range(len(input)):
    if i%2==0:
        even_index.append(input[i])
    else :
        odd_index.append(input[i])
even_index.sort()
even_index.reverse()
odd_index.sort()
output = []
for i in range(len(even_index)):
    output.append(even_index[i])
    output.append(odd_index[i])
print(output)

# without extra list
input  = [10,36,45,3,2,1,12,20,50,16]
for i in range(0, len(input), 2):
    for j in range(i+2, len(input), 2):
        if input[i] < input[j]:
            input[i], input[j] = input[j], input[i]
for i in range(1, len(input), 2):
    for j in range(i+2, len(input), 2):
        if input[i] > input[j]:
            input[i], input[j] = input[j], input[i]
print(input)