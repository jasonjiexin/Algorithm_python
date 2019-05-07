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


# In[56]:


'''
木桶排序（）
'''
# 定义列表
num_list=[6,9,8,7,2,5,1]
# 测试列表
print(num_list)

# 列表的长度
length = len(num_list)
print(length) # 测试列表长度

# 定义空桶,因为元素中有9，所以需要至少10个桶
Bucket = [0,0,0,0,0,0,0,0,0,0]
#Bucket[1] = 1
print(Bucket)

for i in range(length):        
#     用列表num_list的值用作，“木桶”的下标
    value = num_list[i]
#     将对应的值给对应的“桶”，3在3号桶
    Bucket[value] =num_list[i]

# 打印排序后的序列，没有去处零
print(Bucket)

# 打印排序后的列表
length_Bucket = len(Bucket)
for j in range(length_Bucket):
    if Bucket[j] == 0:
        continue

    print(Bucket[j],end=",  ")

  
    
# 未解决问题：如果给定的列表中有0怎样处理会更简便？
    


# In[17]:


'''
选择排序
'''

# 思想：找到极值（极大值、极小值）的然后跟换下标，每一趟全部比较完后，再将元素放在开头或者结尾

# 定义一个列表
m_list =[[1,9,8,5,6,7,4,3,2],[1,2,3,4,5,6,7,8,9]]

# 把列表的值取出来
nums = m_list[0]
# 求列表的长度
length = len(nums)

print(nums)
print(length)

# 由于该算法主要耗时间的地方就是比较和交换，做标记变量
count_swap = 0    #交换
count_iter = 0   #比较


# 列表值比较
for i in range(length):
#     定义最大数字的索引
    maxindex = i
    for j in range(i+1,length):   #for j in range(1, length-i) 与前面语句执行结果一致
        count_iter += 1  #比较计数
#         最大数字与下标为j数字进行比较
        if nums[maxindex] < nums[j]:
               maxindex = j
#     减少交换次数，如果i=maxindex 不用进行交换        
    if i != maxindex:
        tmp = nums[i]
        nums[i] = nums[maxindex]
        nums[maxindex] = tmp
        count_swap += 1   #交换计数
        
print(nums,count_iter,count_swap)
        

