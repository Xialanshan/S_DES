class Keys:
    '''
    将10-bit母密钥拓展成两个8-bit子密钥
    '''
    def __init__(self, key):
        self.key = key

    def P_10(self):
        """
        10-bit置换盒处理规则
        参数: 母密钥
        返回值: 10-bit置换密钥
        """
        key_lst = list(self.key)
        P_box_10 = [3,5,2,7,4,10,1,9,8,6]
        tmp_key = []
        for i in P_box_10:
            tmp_key.append(key_lst[i-1])
        res_key = ''.join(tmp_key)
        return res_key
    
    def LeftShift(self, key):
        """
        拆成左右各半做一次移位
        参数: 10-bit置换密钥
        返回值: 10-bit移位密钥
        """
        key_lst = list(key)
        left = key_lst[:5]
        right = key_lst[5:]
        left.append(left[0])
        left.pop(0)
        right.append(right[0])
        right.pop(0)
        tmp_key = left + right
        res_key = ''.join(tmp_key)
        return res_key
    
    def P_8(self, key):
        """
        8-bit置换盒处理规则
        参数: 10-bit移位密钥
        返回值: 子密钥
        """
        key_lst = list(key)
        P_box_8 = [6,3,7,4,8,5,10,9]
        tmp_key = []
        for i in P_box_8:
            tmp_key.append(key_lst[i-1])
        res_key = ''.join(tmp_key)
        return res_key

# 获取子密钥
def get_keys(mother_key):
    keys = Keys(mother_key)
    key_10 = keys.P_10()
    key_shift1 = keys.LeftShift(key_10)
    children_key1 = keys.P_8(key_shift1)
    key_shift2 = keys.LeftShift(key_shift1)
    children_key2 = keys.P_8(key_shift2)
    cipher_key = [children_key1, children_key2]
    return cipher_key



    