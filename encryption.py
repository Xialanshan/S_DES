import pandas as pd

data1 = {
    '00': ['01', '11', '00', '11'],
    '01': ['00', '10', '10', '01'],
    '10': ['11', '01', '01', '00'],
    '11': ['10', '00', '11', '10']
}
row_index1 = ['00', '01', '10', '11']
S_box1 = pd.DataFrame(data1, index=row_index1)

data2 = {
    '00': ['00', '10', '11', '10'],
    '01': ['01', '11', '00', '01'],
    '10': ['10', '01', '01', '00'],
    '11': ['11', '00', '10', '11']
}
row_index2 = ['00', '01', '10', '11']
S_box2 = pd.DataFrame(data2, index=row_index2)


def PlainTextTransfer(plaintext:str, form):
    """
    如果明文是ASII码,就需要先做ASII码到二进制字符串的转换,一个ASII码就是一个8-bit分组
    """
    if form == 'Binary':
        return plaintext
    else:
        res = str()
        for i in plaintext:
            res += format(ord(i), '08b')
        return res
    
    
def CipherTextTransfer(ciphertext:str, form):
    if form == 'Binary':
        return ciphertext
    else:
        res = str()
        for i in range(0, len(ciphertext),8):
            res += chr(int(ciphertext[i:i+8],2))
        return res
    

class Cipher:
    """
    将明文加密成密文
    输入: 明文、密钥
    输出: 密文
    """
    def __init__(self, plaintext, keys):
        """
        plaintext是经过函数处理的明文
        keys是从getKeys.py里面导入的子密钥列表[key0, key1]
        """
        self.plaintext = plaintext
        self.keys = keys

    def split(self, plaintext):
        """
        将二进制明文分组: 8-bit为一组, 最后不足的补成8位
        参数: 明文
        返回值: 分组列表
        """
        pt_lst = []     # 分组列表: 存储每一个8-bit子串
        length = len(plaintext)
        if length % 8 == 0:
            for i in range(0, length, 8):
                pt_lst.append(plaintext[i:i+8])
        else:
            for i in range(0, length - 8, 8):
                pt_lst.append(plaintext[i:i+8])
            rest = length % 8
            pt_lst.append('0' * (8-rest) + plaintext[length - rest:])
        return pt_lst
    
    def IP(self, subplaintext):
        """
        初始置换规则: IP = (2,6,3,1,4,8,5,7)
        参数: 8-bit的分组二进制字符串
        返回值: 经过置换的分组
        """
        IP_box = [2,6,3,1,4,8,5,7]
        text_lst = list(subplaintext)
        tmp_text = []
        for i in IP_box:
            tmp_text.append(text_lst[i-1])
        res_text = ''.join(tmp_text)
        return res_text
    
    def func_encrypt(self, subplaintext, flag_key):
        """
        参数: 经过初始置换的8-bit分组; flag_key标记使用哪个子密钥 keys[flag_key]
        返回值: 经过加密的8-bit分组
        """
        # step1: 切割成左右两个小分组
        text_lst = list(subplaintext)
        left = text_lst[:4]
        right = text_lst[4:]

        # step2: 对右小组做4-8bit的拓展置换
        EP_box = [4,1,2,3,2,3,4,1]
        tmp_right = []
        for i in EP_box:
            tmp_right.append(right[i-1])
        tmp_right = ''.join(tmp_right)
        
        # step3: 用轮密钥与右分组做异或处理
        tmp_text = ''.join('1' if bit1 != bit2 else '0' for bit1, bit2 in zip(tmp_right, self.keys[flag_key]))

        # step4: 压缩替换 8-4bit
        subs_value = S_box1.loc[tmp_text[0]+tmp_text[3], tmp_text[1:3]] + S_box2.loc[tmp_text[4]+tmp_text[7], tmp_text[5:7]]

        # step5: 直接替换
        SP_box= [2,4,3,1]
        value_lst = list(subs_value)
        tmp = []
        for i in SP_box:
            tmp.append(value_lst[i-1])
        tmp = ''.join(tmp)

        # step6: 替换后的4-bit与left做异或处理得到加密后的左分组
        left = ''.join(left)
        en_left = ''.join('1' if bit1 != bit2 else '0' for bit1, bit2 in zip(tmp, left))

        # step7: 判断是否需要左右互换,最后输出
        right = ''.join(right)
        if flag_key == 0:
            return right + en_left
        else:
            return en_left + right
    
    def FP(self, subplaintext):
        """
        最终置换: IP^(-1) = (4,1,3,5,7,2,8,6)
        参数: 经过加密函数处理的8-bit分组
        返回值: 该分组对应的密文
        """
        FP_box = [4,1,3,5,7,2,8,6]
        text_lst = list(subplaintext)
        tmp_text = []
        for i in FP_box:
            tmp_text.append(text_lst[i-1])
        res_text = ''.join(tmp_text)
        return res_text

    def transfer(self):
        """
        将每个分组的8-bit子串的加密结果进行整合输出, 得到最终密文
        """
        pt_lst = self.split(self.plaintext)
        # print(pt_lst)
        res = []
        for i in pt_lst:
            i = self.IP(i)
            i = self.func_encrypt(i, 0)
            i = self.func_encrypt(i, 1)
            i = self.FP(i)
            res.append(i)
        res = ''.join(res)
        return res



    


        
