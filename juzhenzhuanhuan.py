'''
M=N 矩阵（方阵）元素转换
'''
#写法1，打印的方法
# 生成两维矩阵
lst = [[1, 2, 3]]
for i in range(2):
    pre = lst[i]
    cur = []
    for j in range(3):
        cur.append(pre[j] + 3)
    lst.append(cur)
print(lst)

print("====="*20)

# 横着打印
for i in range(3):
    for j in range(3):
        print(lst[i][j], end = " ")
    print()

print("====="*20)
    
# 竖着打印
for i in range(3):
    for j in range(3):
        print(lst[j][i], end = " ")
    print()


# 写法2，enumerate方法
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(matrix)
count = 0
for i, row in enumerate(matrix):
    for j, col in enumerate(row):
        if i < j:
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp
            count += 1
print(matrix)
print(count)

# 写法2 ，交换部分用到封装和解构
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(matrix)
count = 0
for i, row in enumerate(matrix):
    for j, col in enumerate(row):
        if i < j:
# 交换语句
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            count += 1
print(matrix)
print(count)

# 写法3，不用enumerate方法
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(matrix)
matrix_len = len(matrix)
print(matrix_len)
count = 0
for i in range(matrix_len):
    for j in range(matrix_len):
        if i < j:
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            count += 1
print(matrix)
print(count)
