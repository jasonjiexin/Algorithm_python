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
    


# In[24]:


'''
选择排序
'''

# 思想：找到极值（极大值、极小值）的然后，更换下标，每一趟全部比较完后，再将元素放在开头或者结尾

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
count_times = 0  #趟数、轮数


# 列表值比较
for i in range(length):
#     定义最大数字的索引
    count_times += 1
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
        
print(nums,count_iter,count_swap,count_times)
        


# In[19]:


'''
选择排序-二元选择排序
'''

# 二元选择排序是为了降低比较的次数，因此每轮比较极大值和极小值一起进行比较，理论上极大值、极小值一起开始比较趟数是之前趟数的一半就可以完成排序，

# 定义一个列表
m_list = [[1,9,8,5,6,7,4,3,2],[1,2,3,4,5,6,7,8,9],[9,8,7,6,5,4,3,2,1]]

#取出列表
nums = m_list[0]  # [1,9,8,5,6,7,4,3,2]

# 计算列表的长度
length = len(nums)

# 设定元素比较和元素交换的变量
count_swap = 0
count_iter = 0
count_times = 0  #趟数、轮数

# 二元选择排序主体
for i in range(length // 2):  #趟数、轮数
#     默认定义列表两头分别是极大值和极小值
    count_times += 1
    maxindex = i
    minindex = -i - 1
    #maxindex 表示最大值的坐标，i元素表示从前到后迭代的元素坐标，因此minindex 表示最小值的坐标，minorigin 表示从后到前迭代的元素坐标
    minorigin = minindex  
    
    for j in range(i+1,length-i):    #代表每一趟比较后，列表首部和末尾都会各少一个在下趟中被比较的元素
        count_iter += 1
        
#         确定好最大值和最小值的下标
        if nums[maxindex] < nums[j]:   #用最大值与下一个元素比较
            maxindex = j
        if nums[minindex] > nums[-j -1]:   #用最小值与上一个元素比较
            minindex = -j -1
    
    print(maxindex,minindex)
    
    if i != maxindex:
        tmp = nums[i]
        nums[i] = nums[maxindex]
        nums[maxindex] = tmp
        count_swap +=1
        
        #如果最小值被交换过，要更新索引，（如果i 代表的是 元素正是最小值的索引，那么会被最大值索引替换，在下面进行最小值交换时就会有问题，因此要进行索引更新）
        if i == minindex or i == length +minindex:  #i == minindex  正索引的情况    i == length +minindex  负索引的情况，负索引是不能和正索引进行比较的
            minidex = maxindex
            
    if minorigin != minindex:
        tmp = nums[minorigin]
        nums[minorigin] = nums[minindex]
        nums[minindex] = tmp
        count_swap +=1
        
print(nums, count_iter,count_swap,count_times)  #趟数由36变为20次


# In[ ]:




