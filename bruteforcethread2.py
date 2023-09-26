import deciphering
import time
import threading

"""
暴力破解，多线程
对于每个明文密文对，都会创建一个单独的线程来处理
"""


# 暴力破解并过滤密钥的函数
def decrypt_and_filter(plaintext, ciphertext, valid_keys, lock, i):
    """
    :param plaintext: 明文列表，包含多个明文字符串。
    :param ciphertext: 密文列表，包含多个密文字符串，与明文对应。
    :param valid_keys: 一个列表，用于存储满足特定明文密文对的密钥集合。
    :param lock: 一个锁对象，用于多线程同步，以确保对共享数据的安全访问。
    :param i: 当前处理的明文密文对的索引。
    """
    keys_to_remove = []
    if i == 0:
        for key in range(1024):
            binary_key = format(key, '010b')
            decrypted_text = deciphering.binarystring(ciphertext[i], binary_key)
            if decrypted_text == plaintext[i] and key <= 1024:
                valid_keys.append(binary_key)
    else:
        for key in valid_keys:
            decrypted_text = deciphering.binarystring(ciphertext[i], key)
            if decrypted_text != plaintext[i]:
                keys_to_remove.append(key)

        # 使用锁来避免多线程下的竞态条件
        with lock:
            for key_to_remove in keys_to_remove:
                valid_keys.remove(key_to_remove)


# 多线程暴力破解函数。
def brute_force(plaintext, ciphertext):
    """
        :param plaintext: 明文列表，包含多个明文字符串。
        :param ciphertext: 密文列表，包含多个密文字符串，与明文对应。
        该函数的主要作用是使用多线程并行处理多个明文密文对，调用 decrypt_and_filter 函数进行解密和过滤密钥的操作，并返回最终的密钥结果。
        :return: 一个列表，包含满足所有明文密文对的密钥集合。
        """
    valid_keys = []
    lock = threading.Lock()  # 创建一个锁对象，用于多线程同步
    threads = []

    for i in range(len(plaintext)):
        thread = threading.Thread(target=decrypt_and_filter, args=(plaintext, ciphertext, valid_keys, lock, i))
        threads.append(thread)

    # 启动线程
    for thread in threads:
        thread.start()

    # 等待所有线程完成
    for thread in threads:
        thread.join()

    return valid_keys


"""plaintext=['10111001','11111100','01101010']
ciphertext=['01011000','10101010','01010101']"""

n = input("已知明密文对数量：")
plaintext = []
ciphertext = []
i = 0
while i < int(n):
    plain_input = input(f"请输入第{i + 1}个明文：")
    cipher_input = input(f"请输入第{i + 1}个密文：")
    plaintext.append(plain_input)
    ciphertext.append(cipher_input)
    i = i + 1

start_time = time.time()
result = brute_force(plaintext, ciphertext)
end_time = time.time()

# 计算运行时间
elapsed_time = end_time - start_time
print(result)
print("多线程暴力破解时间：", elapsed_time)
