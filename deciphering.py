import getkey

# 逐位异或操作函数
def xor_bits(a, b):
    """
    :param a: 二进制数
    :param b: 二进制数
    :return: a与b异或的结果
    """
    result = ""
    for i in range(len(a)):
        result += str(int(a[i]) ^ int(b[i]))
    return result

# 初始逆置换函数
def initial_permutation(ciphertext):
    """
    :param ciphertext: 输入8bit二进制密文
    :return: 返回经过初始置换后的明文
    """
    IP = [2, 6, 3, 1, 4, 8, 5, 7]
    return ''.join(ciphertext[i - 1] for i in IP)

# 最终逆置换函数
def final_permutation_inv(ciphertext):
    """
    :param ciphertext: 输入8bit二进制
    :return: 返回最终置换后的结果
    """
    IP_inv = [4, 1, 3, 5, 7, 2, 8, 6]
    return ''.join([ciphertext[i - 1] for i in IP_inv])


# SPBox置换函数
def permute_SPBox(input_text):
    """
    :param input_text: 4bit二进制数
    :return: 返回置换后的4bit二进制数
    """
    SPBox = [2, 4, 3, 1]
    return ''.join([input_text[i - 1] for i in SPBox])

# S-盒替换函数
def sbox_substitution(input_text, sbox):
    """
    :param input_text: 需要替换的二进制4bit
    :param sbox: 使用的替换盒
    :return: 返回替换后的二进制数2bit
    """
    row = int(input_text[0] + input_text[3], 2)
    col = int(input_text[1] + input_text[2], 2)
    return format(sbox[row][col], '02b')  # 以二进制格式返回

# F 函数，接受一半和子密钥作为输入
def F(right_half, key):
    """
    :param right_half: 需要输入的右半部分 4bit
    :param key: 子密钥
    :return: 返回经过轮函数的结果 4bit
    """
    # 从4bit扩展为8bit
    EPBox = [4, 1, 2, 3, 2, 3, 4, 1]
    expanded_half = ''.join([right_half[i - 1] for i in EPBox])

    # 与子密钥异或
    xored_half = xor_bits(expanded_half, key)

    # 划分为两部分
    left_xored_half = xored_half[:4]
    right_xored_half = xored_half[4:]

    # S-盒替换，每部分4bit变为2bit
    SBox1 = [[1, 0, 3, 2],
            [3, 2, 1, 0],
            [0, 2, 1, 3],
            [3, 1, 0, 2]]
    SBox2 = [[0, 1, 2, 3],
            [2, 3, 1, 0],
            [3, 0, 1, 0],
            [2, 1, 0, 3]]
    sbox_output_left = sbox_substitution(left_xored_half, SBox1)
    sbox_output_right = sbox_substitution(right_xored_half, SBox2)

    # SPBox置换
    SPBox_output = permute_SPBox(sbox_output_left + sbox_output_right)

    return SPBox_output

# 解密函数，接受密文和两个子密钥
def decrypt(ciphertext, key1, key2):
    """
    :param ciphertext: 密文8bit
    :param key1:子密钥1
    :param key2:子密钥2
    :return: 返回对应的明文 8bit
    """

    initial_permuted = initial_permutation(ciphertext)

    left_half = initial_permuted[:4]
    right_half = initial_permuted[4:]

    f1_output = F(right_half, key2)

    left_output = xor_bits(left_half, f1_output)

    left_half, right_half = right_half, left_output

    f2_output = F(right_half, key1)
    left_output2 = xor_bits(left_half, f2_output)

    merged_half = left_output2 + right_half

    # 初始逆置换
    plaintext = final_permutation_inv(merged_half)

    return plaintext

# 对字符串进行解密
def decryptstring(cipherString, key):
    """
    :param cipherString: 密文字符串
    :return: 返回明文字符串
    """
    key1, key2 = getkey.generate_keys(key)
    plainstring = ""
    for char in cipherString:
        ciphertext = format(ord(char), '08b')

        plaintext = decrypt(ciphertext, key1, key2)
        plaintChar = chr(int(plaintext, 2))
        plainstring = plainstring + plaintChar

    return plainstring

# 对二进制字符串进行解密
def binarystring(cipherString, key):
    """
    :param cipherString: 二进制串的密文
    :param key: 密钥
    :return:二进制字符串的明文
    """
    length=len(cipherString)
    key1, key2 = getkey.generate_keys(key)
    number = length // 8
    plainbinarystring = ""
    for i in range(0, length, 8):
        group = cipherString[i:i + 8]   #取一组8bit
        plain_group=decrypt(group,key1,key2)
        plainbinarystring=plainbinarystring+plain_group
    return plainbinarystring

def user_decryption(symbol,ciphertext,key):
    """
    :param symbol: 标志是二进制还是ASCII
    :return: 返回的解密结果
    """
    if symbol=="Binary":
        return binarystring(ciphertext,key)
    else:
        return decryptstring(ciphertext,key)


