'''
Author: xidianwxm 1004700452@qq.com
Date: 2024-08-06 10:58:30
LastEditors: xidianwxm 1004700452@qq.com
LastEditTime: 2024-08-06 11:03:23
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



import threading
import time



# 唱歌任务，循环五次跳舞，每次休息10秒
def sing():
    # 扩展： 当前线程
    # print("sing当前执行的线程为：", threading.current_thread())
    for i in range(5):
        print("正在唱歌...%d" % i)
        time.sleep(10)


# 跳舞任务，循环五次跳舞，每次休息10秒
def dance():
    # 扩展： 当前线程
    # print("dance当前执行的线程为：", threading.current_thread())
    for i in range(10):
        print("正在跳舞...%d" % i)
        time.sleep(5)


if __name__ == '__main__':
    # 扩展： 当前线程
    # print("当前执行的线程为：", threading.current_thread())
    # 创建唱歌的线程
    # target： 线程执行的函数名
    sing_thread = threading.Thread(target=sing)

    # 创建跳舞的线程
    dance_thread = threading.Thread(target=dance)

    # 开启线程
    sing_thread.start()
    dance_thread.start()