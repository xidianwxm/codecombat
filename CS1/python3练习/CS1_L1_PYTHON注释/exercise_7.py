'''
程序说明
'''
# -*- coding: utf-8 -*-
# -*- coding: UTF-8 -*-
# Windows系统上路径
#!D:\gtjasoft\python\python312\python3
# Linux系统上路径
#!/usr/bin/python3

def calculate_sum(a , b):
    """
    函数说明：
        计算两个数数值的和。

    参数:
        a (int): 被加数。
        b (int): 加数
    
    返回:
        int: 和。

    示例:
    >>> calculate_sum(3，6)
    9
    """
    
    return a + b

# 这个函数copy的上面的部分，只完成了一半，请你帮忙修改逻辑和语法，使其正确
def calculate_sub(a , b):
    """
    函数说明：
        计算两个数数值的差。

    参数:
        a (int): 被加数。
        b (int): 加数
    
    返回:
        int: 和。

    示例:
    >>> calculate_sum(3，6)
    9
    """
    
    return a + b


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
