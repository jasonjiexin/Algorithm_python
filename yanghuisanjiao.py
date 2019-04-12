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
    

'''
获取杨辉三角中第m行，第k列的值
解决思路先构造出第m行，再进行取值
从第三行开始构造，triangle中先指定两个元素 triangle=[[1][1,1]]
'''
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


'''
获取杨辉三角中第m行，第k列的值
解决思路先构造出第m行，再进行取值
从第一行开始构造，triangle=[]
'''
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


'''
获取杨辉三角中第m行，第k列的值
补零的方法来实现，零刚好在对位j 和 j-2的值是相同的
'''
pre = [1]
cur = [1]
m = 6
k = 6

# print(pre)

# 分为三个部分：k<m and k!=m ，k==m or k==1，k>m

if k < m and k != 1:
# 要拿到第六层的数据只需要计算到第五层就好了，除了i=1，剩下需要计算四层（m-1）
    for i in range(1, m - 1):
        pre.append(0)
        cur.append(1)
        if i != 1:
            for j in range(1, i // 2 + 1):
                cur[j] = pre[j - 1] + pre[j]
# 当改位置是对称位时才能够执行下边的操作，补全对称位，对称位值相等
                if 2 * j != i:
                    cur[-j - 1] = cur[j]

# 当前的list(cur)变为之前的list(pre),这种写法是Python的一个特性，相当于两个variables相互交换
        cur, pre = pre, cur

    print("yang hui triangle's {}th line {}th num is {}".format(m, k, pre[k - 2] + pre[k - 1]))
# 取头和取尾都是1
elif m == k or k == 1:
    print("yang hui triangle's {}th line {}th num is 1".format(m, k))
else:
    print("k cannot bigger than m!")