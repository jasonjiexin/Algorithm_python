#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 冒泡排序
num_list = [[1,9,8,5,6,7,4,3,2], [1,2,3,4,5,6,7,8,9]]
nums = num_list[0]
print(nums)
length = len(nums)
print(length)
count_swap = 0
count = 0
#bubble sort
#i 为趟数
for i in range(length):
    #j为前后两个元素的编号
    for j in range(length - i -1): #length - i -1 表示每一趟少比较一次，如果不减1列表会超界
        count += 1 #计数的常规做法，意思为比较次数
        if nums[j] > nums[j +1]:
            #数值交换
            tmp = nums[j]
            nums[j] = nums[j + 1]
            nums[j + 1] = tmp
            count_swap += 1 #计数常规做法，意思为交换次数
print(nums,  count_swap, count)


# In[9]:


# 定义一个列表
num_list=[[4,5,9,2,3,8,7,4,6], [6,2,4,1,9,8,3]]

# 取值
num1=num_list[0]
num2=num_list[1]

# 测试列表是否取值正常
print(num1)
print(num2)

# 计算两个列表的长度
length1=len(num1)
length2=len(num2)

# 打印列表长度
print(length1)
print(length2)

# 定义计数标识，元素比较的次数、交互数
count = 0
count_swap = 0

# 定义比较的趟数，取值范围为length-1
for i in range(length1):
#     定义元素比较的次数
    for j in range(length1-1-i):
        count += 1
        if num1[j] > num1[j+1]:
            
            swap = num1[j]
            num1[j] = num1[j+1]
            num1[j+1] = swap
#             记录元素交换的次数
            count_swap += 1

print("排序结果如下:")
print(num1,count,count_swap)

# 定义计数标识，元素比较的次数、交互数，归零
count = 0
count_swap = 0

# 定义比较的趟数，取值范围为length-1
for i in range(length2):
#     定义元素比较的次数
    for j in range(length2-1-i):
        count += 1
        if num2[j] > num2[j+1]:
#             元素交换
            num2[j],num2[j+1] = num2[j+1],num2[j]
#             记录元素交换的次数
            count_swap += 1

print("排序结果如下:")
print(num2,count,count_swap)


# In[ ]:




