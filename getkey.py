def generate_keys(key):
    """
    :param key: 输入密钥
    :return: 输出两个子密钥key1,key2
    """

    # 循环左移函数
    def left_shift(lst,n):
        """
        :param lst:需要变化的二进制
        :param n:左移位数
        :return:返回移动后的结果
        """
        return lst[n:] + lst[:n]

    # 初始置换P10
    P10 = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]       # 初始置换表P10
    permuted_key = ['0'] * 10
    for i, pos in enumerate(P10):
        permuted_key[i] = key[pos - 1]

    # 分割成左右两部分
    left_half = permuted_key[:5]
    right_half = permuted_key[5:]

    # 循环左移一位
    left_half = left_shift(left_half,1)
    right_half = left_shift(right_half,1)

    # 合并左右两部分
    merged_key = left_half + right_half

    # P8置换，生成子密钥k1
    P8 = [6, 3, 7, 4, 8, 5, 10, 9]              # P8置换表
    key1 = ''.join([merged_key[i - 1] for i in P8])

    # 再次循环左移1位
    left_half = left_shift(left_half,1)
    right_half = left_shift(right_half,1)

    # 合并左右两部分
    merged_key = left_half + right_half

    # 得出第二个子密钥k2
    key2 = ''.join([merged_key[i - 1] for i in P8])

    return key1, key2







