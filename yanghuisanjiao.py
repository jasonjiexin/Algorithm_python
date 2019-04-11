#构造三行的杨辉三角
triangle = [[1],[1,1]]
n = 3
for i in range(2, n):
    pre = triangle[i - 1]
    cur = [1]
    cur.append(pre[0] + pre[1])
    cur.append(1)
    triangle.append(cur)
    print(triangle)

#构造n行的杨辉三角
triangle = [[1], [1,1]]
n = 5
for i in range(2, n):
    pre = triangle[i - 1]
    cur = [1]
    for j in range(i - 1):
        cur.append(pre[j] + pre[j + 1])
    cur.append(1)
    triangle.append(cur)
    print(triangle)


#获取杨辉三角中第m行，第k列的值
#解决思路先构造出第m行，再进行取值
#从第三行开始构造，triangle中先指定两个元素 triangle=[[1][1,1]]
triangle = [[1], [1,1]]
n = 5
k = 2
for i in range(2, n):
    pre = triangle[i - 1]
    cur = [1]
    for j in range(i - 1):
        cur.append(pre[j] + pre[j + 1])
    cur.append(1)
    triangle.append(cur)
print(triangle[n - 1][k - 1])


#获取杨辉三角中第m行，第k列的值
#解决思路先构造出第m行，再进行取值
#从第一行开始构造，triangle=[]
m = 5
k = 4
#空列表开始开始负
triangle = []

# i 为行坐标下标
for i in range(m):
    row = [1]
    triangle.append(row)
    if i == 0:
#结束本次循环
        continue
# j 的取值范围虽然（1，i）与（i - 1）取值的个数是一致的，但是（i - 1）会发生取负索引的情况，j是从0开始取值的，j-1=-1计算时会取列表中的最后一个元素
# j 为纵坐标下标
    for j in range(1, i):
        row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
    row.append(1)
print(triangle[m-1][k-1])

