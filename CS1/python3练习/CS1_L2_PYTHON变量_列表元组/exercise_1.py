'''
Author: xidianwxm 1004700452@qq.com
Date: 2024-08-06 17:00:28
LastEditors: xidianwxm 1004700452@qq.com
LastEditTime: 2024-08-06 17:01:20
FilePath: \hello-algo-main\codes\python\codacombat\python3\CS1_L2_PYTHON变量_列表元组\exercise_1.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''

'''
程序说明
'''


# -*- coding: UTF-8 -*-

#!/usr/bin/python3 

'''
'''


# 请猜猜a、b、c分别是多少
a = b = c = 3
c = 4
b = c
print(a)
print(b)
print(c)




# 两个整型对象 2 和 1 分别分配给变量 a 和 c，字符串对象 "Tom" 分配给变量 b。
# 请猜猜a、b、c分别是多少
a, b, c = 2, "Tom", 21
print(a)
print(b)
print(c)

# 请猜猜a、b、c分别是多少
a, c = c, a
print(a)
print(b)
print(c)


# 代码怎么了
# 两个整型对象 1 和 2 分别分配给变量 a 和 b，字符串对象 "john" 分配给变量 c。
a, b, c = 1, 2
# 猜猜a,b,c是？
print(a)
print(b)
print(c)

# 这样呢
# 猜猜a,b,c是？
a, b, c = 1, 2, 3, 4
print(a)
print(b)
print(c)





