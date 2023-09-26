import deciphering
import time

"""
暴力破解，非多线程
"""

# 暴力破解的函数
def brute_force(plaintext, ciphertext):
    """
    :param plaintext: 明文列表
    :param ciphertext: 密文列表
    :return: 所有返回能满足输入明密文对的密钥
    """
    length = len(ciphertext)
    i = 0
    valid_keys = []
    while i < length:
        keys_to_remove = valid_keys[:]
        if i == 0:
            for key in range(1024):  # 10位密钥共有2^10种组合
                binary_key = format(key, '010b')  # 将整数密钥转换为10位二进制
                decrypted_text = deciphering.binarystring(ciphertext[i], binary_key)  # 使用S-DES解密函数，根据你的库调整
                if (decrypted_text == plaintext[i]) & (key <= 1024):
                    valid_keys.append(binary_key)
        else:
            for key in keys_to_remove:
                decrypted_text = deciphering.binarystring(ciphertext[i], key)
                if (decrypted_text != plaintext[i]):
                    valid_keys.remove(key)
        i = i + 1

    return valid_keys


"""plaintext=['10111001','11111100','01101010']
ciphertext=['01011000','10101010','01010101']"""
n = input("已知明密文对数量：")
plaintext = []
ciphertext = []
i = 0
# 输入明密文对
while i < int(n):
    plain_input = input(f"请输入第{i + 1}个明文：")
    cipher_input = input(f"请输入第{i + 1}个密文：")
    plaintext.append(plain_input)
    ciphertext.append(cipher_input)
    i = i + 1

# 破解，计时
start_time = time.time()
result = brute_force(plaintext, ciphertext)
end_time = time.time()

# 计算运行时间
elapsed_time = end_time - start_time
print("可能的密钥：", result)
print("暴力破解时间：", elapsed_time)
