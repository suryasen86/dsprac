x=[
    [11,2,54],
    [2,4,6],
    [3,56,8]
    ]

y=[
    [4,6,87],
    [8,9,7],
    [4,8,9]
    ]

result=[
    [0,0,0],
    [0,0,0],
    [0,0,0]]

print('matrix additon')
# matix addition
for i in range(len(x)):
    for j in range(len(y)):
        result[i][j] = x[i][j]+y[i][j]

for i in result:
    print(i)

# matrix multiplication

print('matrix multiplication')

for i in range(len(x)):
    for j in range(len(y)):
        result[i][j] = x[i][j]*y[i][j]

for i in result:
    print(i)


print('matrix transpose ')

z=[[1,2,3],[4,5,6],[7,8,9]]
 
result2=[
    [0,0,0],
    [0,0,0],
    [0,0,0]]

for i in range(len(z)):
    for j in range(len(result2)):
     result2[i][j] = z[j][i]

for i in result2:
    print(i)
