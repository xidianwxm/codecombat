'''
Author: xidianwxm 1004700452@qq.com
Date: 2024-08-06 10:58:30
LastEditors: xidianwxm 1004700452@qq.com
LastEditTime: 2024-08-06 11:00:00
FilePath: \hello-algo-main\codes\python\codacombat\python3\CS1_L1_PYTHON注释\exercise_8.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
'''
程序说明
'''
# -*- coding: utf-8 -*-
# -*- coding: UTF-8 -*-
# Windows系统上路径
#!D:\gtjasoft\python\python312\python3
# Linux系统上路径
#!/usr/bin/python3

# -*- coding: UTF-8 -*-

#!/usr/bin/python



# 局部块之间用三行空行进行分割
import multiprocessing
import time

# 定义全局变量
g_list = list()  # 和代码之间空两个空格，说明g_list的内容

# 函数之间空两行进行分割
# 添加数据的任务
def add_data():
    for i in range(5):
        g_list.append(i)
        print("add:", i)
        time.sleep(0.2)

    # 代码执行到此，说明数据添加完成
    print("add_data:", g_list)

# 函数之间空两行进行分割
def read_data():
    print("read_data", g_list)

if __name__ == '__main__':
    # 由原子函数组合成的逻辑块放一起，中间不用空行分割
    # 创建添加数据的子进程
    add_data_process = multiprocessing.Process(target=add_data)
    # 创建读取数据的子进程
    read_data_process = multiprocessing.Process(target=read_data)

    # 启动子进程执行对应的任务
    add_data_process.start()

    # 主进程等待添加数据的子进程执行完成以后程序再继续往下执行，读取数据
    add_data_process.join()
    read_data_process.start()
    print("main:", g_list)

    # 总结: 多进程之间不共享全局变量

if __name__ == "__main__":
    # 计算 4 + 5等于几？
    x = 4
    y = 5
    z = calculate_sum(y, x)
    print("%d + %d = %d" % (x, y, z))
    

    # 计算 310 - 115等于几？
    # TODO: 减法程序只完成了一半，请你继续 @Abby
    x = 4
    y = 5
    z = calculate_sum(y, x)
    print("%d + %d = %d" % (x, y, z))
