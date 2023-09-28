# S_DES
## 作业报告
#### 第一关：基本测试

GUI界面设计：

![image](https://github.com/Xialanshan/S_DES/assets/110965468/2e2002f7-71e8-4ebd-a651-cc78c12eea20)
​
<p align="center">图1 GUI界面</p>




当输入的message和密钥不符合规范时，会报错并提示重新输入（图2，图3）：

![image](https://github.com/Xialanshan/S_DES/assets/110965468/ebfa81c8-223d-4b9e-9d2c-b64c1afceb4c)

​<p align="center">图2 message不合规</p>

![image](https://github.com/Xialanshan/S_DES/assets/110965468/3c0f96c9-f6cd-4353-9aba-47466de29120)

<p align="center">图3 密钥不合规</p>


测试明文：10111001 测试密文：01011000


密钥：1000101010


生成密文：01011000 生成明文：10111001


加解密结果匹配！

![image](https://github.com/Xialanshan/S_DES/assets/110965468/246ecea9-61d3-4488-8b12-af9997fef76d)


​															<p align="center">图4 加密</p>

![image](https://github.com/Xialanshan/S_DES/assets/110965468/f48661f9-2b8b-48f8-acd5-76e94514eb8c)


​															<p align="center">图5 解密</p>




#### 第二关 交叉测试

我们组的二进制和ASCII码明文加密测试：

![image](https://github.com/Xialanshan/S_DES/assets/110965468/2cf963a7-50c8-404b-9304-a356ad76cf8e)


​														<p align="center">图6 此程序二进制加密</p>

![image](https://github.com/Xialanshan/S_DES/assets/110965468/380412f8-e1c9-47d7-992c-36ec8d56fac9)


​													<p align="center">图7 此程序ASCII码加密</p>

交叉测试组的加密结果：

![image](https://github.com/Xialanshan/S_DES/assets/110965468/dce6c5a1-5e62-4547-aea2-468ef07b87c9)


​												<p align="center">图8 交叉测试组二进制加密</p>

![image](https://github.com/Xialanshan/S_DES/assets/110965468/4c6fbbd2-711e-4b6d-a40a-1649fcfe5eea)


​												<p align="center">图9 交叉测试组ASCII加密</p>

结果：交叉测试通过！



#### 第三关 拓展功能

我们的程序允许输入任意长度的ASCII码字符串，并给出对应的ASCII码字符串密文(明文)，密钥要求是10-bit二进制

测试明文：svc 测试密文：Æþé

密钥：1111111111

生成密文：Æþé 生成明文：svc

加解密结果匹配

但是，由于ASCII在网页中的显示问题和ASCII拓展码有不可见字符的特点，有相当一部分ASCII的加解密无法在我们的本地网页中直接显示。

![image](https://github.com/Xialanshan/S_DES/assets/110965468/88f1c4d6-8406-4e32-a7eb-075b26dddba3)


​													<p align="center">图10 ASCII码字符串加密</p>

![image](https://github.com/Xialanshan/S_DES/assets/110965468/21686634-bae2-448f-b040-436dfb9ec64b)


​													<p align="center">图11 ASCII字符串解密</p>



#### 第四关 暴力破解

在第4关中，我们尝试使用暴力破解的方法来找到正确的密钥。我们找到了三对使用相同的明密文对（见表1）,并使用单线程与多线程的方式对比破解效率。

​				表1 使用相同密钥的明密文对

| 明文 | 10111001 | 11111100 | 01101010 |
| ---- | -------- | -------- | -------- |
| 密文 | 01011000 | 10101010 | 01010101 |

测试的结果如下：

- 使用单线程的暴力破解，共用时0.01940秒；

- 使用多线程的暴力破解，共用时0.0440秒；

- 找到的密钥Key有：\[1000101010, 1100101010\]

单线程：

![image](https://github.com/Xialanshan/S_DES/assets/110965468/25466a49-d393-4eb5-b217-e3301593fc55)


​										<p align="center">图12 单线程暴力破解</p>

多线程：[https://youtu.be/w4pntuSSv1s](https://youtu.be/w4pntuSSv1s)




#### 第五关：封闭测试

在第5关中，根据第4关的结果，我们进一步分析了是否可能存在不止一个密钥Key，以及在明文空间中是否会出现不同的明文分组Pn，加密得到相同密文Cn的情况。

根据第4关的明密文对，和暴力破解的结果，得出如下结论：

-  对于一个明文密文对，存在不止一个密钥Key可以成功解密该对。
-  对于明文空间中的多个明文分组Pn，存在不同的密钥Ki和Kj，使得加密得到相同的密文Cn。例如：明文10111001，通过密钥1000101010或1100101010，得到密文01011000。

扩展：

通过进一步分析，我们发现，输入不同的10bit密钥，只要生成的两个子密钥Km，Kn对应相同，就会使得加密相同明文，得到相同的密文。

对于下面5对密钥生成的子密钥：1000101010和1100101010，1111110011和1011110011，1000000010和1100000010，0011100000和0111100000，0010101101和0110101101，分别求出生成的子密钥（见图13）。

通过测试，我们发现当两个10位密钥中只有第2位不同，其他位都相同，它们会生成相同的子密钥。

![image](https://github.com/Xialanshan/S_DES/assets/110965468/76fb6ab5-5741-4f8e-881e-df16304ea532)


​											<p align="center">图13 子密钥生成结果</p>

## 开发手册
#### 1. 算法简介

S-DES是一种经典的分组密码算法，用于对8bits明文数据进行加密和解密。它主要包括两个阶段：密钥生成和数据加密/解密。

1. 密钥生成：
   - 用户提供一个10bits的密钥（K1 K2 K3 K4 K5 K6 K7 K8 K9 K10）
   - 密钥产生两个8bits的子密钥：K1和K2
2. 数据加密：
   - 明文被分为两个4bits的块：L0和R0
   - 对L0和R0执行初始置换（IP）操作。
   - 迭代运算：包括扩展、异或、S-盒替代、P-盒置换和异或操作。
   - 交换左右半块，并再次进行迭代运算
   - 最终的左半块（L4）和右半块（R4）被合并并经过逆初始置换（IP^-1）操作，生成8位的密文。
3. 数据解密：
   - 与数据加密过程类似，但使用子密钥K2（逆序）和K1进行运算。

S-DES算法是一种基础的加密算法，可以用于教育和学术目的，但不适合用于安全要求较高的应用。在实际应用中，通常会使用更强大的加密算法，如AES（Advanced Encryption Standard）。



#### 2. 必要组件

##### 2.1生成密钥

1. 创建密钥生成类

   初始化输入10bits母密钥，调用方法返回两个8bits子密钥

   ```python
   class Keys:
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
   ```

2. 实现获取子密钥函数

   调用密钥生成类，输出10bits母密钥，得到两个8bits子密钥

   ```python
   def get_keys(mother_key):
       keys = Keys(mother_key)
       key_10 = keys.P_10()
       key_shift1 = keys.LeftShift(key_10)
       children_key1 = keys.P_8(key_shift1)
       key_shift2 = keys.LeftShift(key_shift1)
       children_key2 = keys.P_8(key_shift2)
       cipher_key = [children_key1, children_key2]
       return cipher_key
   ```

注意：加解密使用的是两套代码逻辑（由两位同学编写），在密钥生成函数上有所不同，以下为解密代码使用的密钥生成代码：

```python
def generate_keys(key):
    
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
```



##### 2.2加密

1. 创建加密类

   初始化输入8bits整数倍的明文，两个8bits子密钥，调用方法返回密文

   ```python
   class Cipher:
       
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
   ```

2. 对明文格式做处理：如若是二进制字符串，则直接返回；如若是ASCII码字符串，则转换成二进制输出

   ```python
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
   ```

3. 对输出密文格式做处理：与明文格式保持一致

   ```python
   def CipherTextTransfer(ciphertext:str, form):
       if form == 'Binary':
           return ciphertext
       else:
           res = str()
           for i in range(0, len(ciphertext),8):
               res += chr(int(ciphertext[i:i+8],2))
           return res
   ```

   

##### 2.3解密

1. 实现初始置换的函数

   输入8bits二进制密文ciphertext，返回经过初始置换后的明文

   ```python
   def initial_permutation(ciphertext):
       IP = [2, 6, 3, 1, 4, 8, 5, 7]
       return ''.join(ciphertext[i - 1] for i in IP)
   ```

   

2. 实现最终置换的函数

   输入8bits二进制ciphertext,返回最终置换后的结果

   ```python
   def final_permutation_inv(ciphertext):
       IP_inv = [4, 1, 3, 5, 7, 2, 8, 6]
       return ''.join([ciphertext[i - 1] for i in IP_inv])
   ```

   

3.  实现SPBox置换的函数

    输入4bits二进制数，返回置换后的4bits二进制数

    ```python
    def permute_SPBox(input_text):
        SPBox = [2, 4, 3, 1]
        return ''.join([input_text[i - 1] for i in SPBox])
    ```

    

4. 实现S盒替换的函数

   输入需要替换的二进制4bits和使用的替换盒，返回替换后的二进制数2bits

   ```python
   def sbox_substitution(input_text, sbox):
       row = int(input_text[0] + input_text[3], 2)
       col = int(input_text[1] + input_text[2], 2)
       return format(sbox[row][col], '02b')
   ```

   

5. 实现轮函数

   需要输入的右半部分 4bits和一个8bits子密钥，return: 返回经过轮函数的结果 4bits

   ```python
   def F(right_half, key):
       # 从4bits扩展为8bits
       EPBox = [4, 1, 2, 3, 2, 3, 4, 1]
       expanded_half = ''.join([right_half[i - 1] for i in EPBox])
       # 与子密钥异或
       xored_half = xor_bits(expanded_half, key)
       # 划分为两部分
       left_xored_half = xored_half[:4]
       right_xored_half = xored_half[4:]
       # S-盒替换，每部分4bits变为2bits
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
   
   ```

   

6. 实现解密过程

   解密函数，接受8bits密文和两个子密钥，返回二进制形式的明文

   ```python
   def decrypt(ciphertext, key1, key2):
   	#初始置换
       initial_permuted = initial_permutation(ciphertext)
   	#分成左右两部分
       left_half = initial_permuted[:4]
       right_half = initial_permuted[4:]
   	#右部分进行轮变换
       f1_output = F(right_half, key2)
       left_output = xor_bits(left_half, f1_output)
   	#左右部分交换
       left_half, right_half = right_half, left_output
   	#右部分再次轮变换
       f2_output = F(right_half, key1)
       left_output2 = xor_bits(left_half, f2_output)
   	#左右合在一起
       merged_half = left_output2 + right_half
       # 初始逆置换
       plaintext = final_permutation_inv(merged_half)
       return plaintext
   
   ```



7. 进行真正的解密工作前判断输入密文的格式

   ```python
   def user_decryption(symbol,ciphertext,key):
       """
       :param symbol: 标志是二进制还是ASCII
       :return: 返回的解密结果
       """
       if symbol=="Binary":
           return binarystring(ciphertext,key)
       else:
           return decryptstring(ciphertext,key)
   
   
   ```

   

8. 对二进制串解密

   输入二进制串的密文和密钥，返回解密后的二进制字符串的明文

   ```python
   def binarystring(cipherString, key):
       length=len(cipherString)
       key1, key2 = getkey.generate_keys(key)
       number = length // 8
       plainbinarystring = ""
       for i in range(0, length, 8):
           group = cipherString[i:i + 8]   #取一组8bits
           plain_group=decrypt(group,key1,key2)
           plainbinarystring=plainbinarystring+plain_group
       return plainbinarystring
   ```

   

9. 对ASCII串解密

   输入ASCII密文字符串，返回明文ASCII字符串

   ```python
   def decryptstring(cipherString, key):
       key1, key2 = getkey.generate_keys(key)
       plainstring = ""
       for char in cipherString:
           ciphertext = format(ord(char), '08b')
           plaintext = decrypt(ciphertext, key1, key2)
           plaintChar = chr(int(plaintext, 2))
           plainstring = plainstring + plaintChar
       return plainstring
   
   ```

   



#### 3. GUI支持和用户交互

##### 3.1 GUI组件设置

支持用户输入信息、修改信息

1. 输入框：

   - Select form: Binary/ASCII

   - message：待加密明文/待解密密文

   - Key：母密钥

2. 按钮选择：
   - Encrypt
   - Decrypt
3. 输出框：密文/明文

```javascript
    <h1>Encryption and Decryption</h1>
    
    <div class="form-container">
        <div class="form-row">
            <label for="type">Select form:</label>
            <select title="Select the input information form:" name="form" id="form-select">
                <option value="Binary" selected>Binary</option>
                <option value="ASCII">ASCII</option>
            </select>
        </div>
        <div class="form-row">
            <label for="message">Message:</label>
            <input type="text" id="message" placeholder="Enter your message">
        </div>
        <div class="form-row">
            <label for="key">Key:</label>
            <input type="text" id="key" placeholder="Enter your key">
        </div>
    </div>

    <div class="buttons-container">
        <button id="Encrypt" onclick="encryptMessage()">Encrypt</button>
        <button id="Decrypt" onclick="decryptMessage()">Decrypt</button>
    </div>

    <div id="iframeContainer">
        <iframe title="iframe-title" id="iframe" src="about:blank"></iframe>
    </div>
    <br/>
```

组件格式设置：

```css
body {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  margin: 0;
}

h1 {
    font-size: 30px;
    color: #3f5ee9;
    text-align: center;
  }

/* 设置表单容器样式 */
.form-container {
  display: flex;
  flex-direction: column;
  align-items: flex-start; 
  text-align: left;
  margin-top: 20px;

}

/* 设置表单行样式 */
.form-row {
  display: flex;
  align-items: center;
  margin-bottom: 20px;
}

/* 设置标签样式 */
label {
  margin-right: 10px; 
  text-align: right; 
  width: 250px; 
}

select {
  width: 125px;
  height: 30px; 
}

input[type="text"] {
  width: 250px; 
  height: 30px; 
}

/* 设置按钮容器样式 */
.buttons-container {
  display: flex;
  justify-content: space-between;
}

/* 设置按钮样式 */
button {
  padding: 10px 20px;
  background-color: #007bff;
  color: #fff;
  border: none;
  cursor: pointer;
  margin-top: 5px;
  margin-right: 20px;
  margin-bottom: 30px;
}

iframe {
  width: 100%; 
  height: 100%; 
}

```

##### 3.2 实现按钮功能函数

1. 实现前后端通信函数：接收前端网页传回的消息，交给后端函数进行处理，并将处理结果返回到前端显示

 ```javascript
 function sendRequest(form,message,key,action) {
     $.ajax({
         type:"POST",
         url:"/"+action,
         timeout:5000,
         contentType: "application/json",
         data: JSON.stringify({              // 将数据转换为JSON字符串
             form: form,
             message: message,
             key:key
         }),
         success:function(responseData){
             console.log(responseData);
             if (action == 'encryptMessage'){
                 var my_iframe = document.getElementById('iframe');
                 my_iframe.contentDocument.body.innerHTML = "";
                 if (form == 'ASCII'){
                     var encodedString = responseData;
                     var parser = new DOMParser();
                     var decodedDocument = parser.parseFromString('<!doctype html><body>' + encodedString, 'text/html');
                     var responseData = decodedDocument.body.textContent;
                 }
                 my_iframe.contentDocument.body.innerHTML = "密文为: " + responseData;
             }
             else if (action == 'decryptMessage'){
                 var my_iframe = document.getElementById('iframe');
                 my_iframe.contentDocument.body.innerHTML = "";
                 if (form == 'ASCII'){
                     var encodedString = responseData;
                     var parser = new DOMParser();
                     var decodedDocument = parser.parseFromString('<!doctype html><body>' + encodedString, 'text/html');
                     var responseData = decodedDocument.body.textContent;
                 }
                 my_iframe.contentDocument.body.innerHTML = "明文为: " + responseData;
             }
         },
         error: function(xhr, status, error) {
             console.log("Error: " + error);
         }
     });
 }
 ```

2. 实现加密/解密按钮调用对应函数

   ```javascript
   function encryptMessage() {
       event.preventDefault();
       var form = document.getElementById('form-select').value;
       var message = document.getElementById("message").value;
       var key = document.getElementById("key").value;
       if (form === 'Binary' && !isValidBinaryMessage(message)) {
           alert("message(Binary)的长度必须是8的整数倍! 请重新输入");
           return;
       }
   
       if (!isValidKey(key)) {
           alert("密钥必须是Binary(10-bit)! 请重新输入");
           return;
       }
       sendRequest(form, message, key, 'encryptMessage');
   }
   
   function decryptMessage() {
       event.preventDefault();
       var form = document.getElementById('form-select').value;
       var message = document.getElementById("message").value;
       var key = document.getElementById("key").value;
   
       if (form === 'Binary' && !isValidBinaryMessage(message)) {
           alert("message(Binary)的长度必须是8的整数倍! 请重新输入");
           return;
       }
   
       if (!isValidKey(key)) {
           alert("密钥必须是Binary(10-bit)! 请重新输入");
           return;
       }
       sendRequest(form, message, key, 'decryptMessage');
   }
   ```

3. 实现message和Key的格式判断函数：要求输入的信息符合加密/解密的格式规范

   ```javascript
   // message如果是字符串,长度只能是8-bit的整数倍
   function isValidBinaryMessage(message) {
       if (message.length % 8 !== 0 || !/^[01]+$/.test(message)) {
           return false;
       }
       return true;
   }
   // key只能是Binary(10-bit)字符串
   function isValidKey(key){
       if (key.length !== 10 || !/^[01]+$/.test(key)) {
           return false;
       }
       return true;
   }
   ```

4. 实现网页的准备状态：修改了输入消息后，输出框将清空，等待下一次的输出展示

   ```javascript
   $(document).ready(function() {
       $("#form-select, #message, #key").change(function() {
           // 重置iframe内容
           var my_iframe = document.getElementById("iframe");
           my_iframe.srcdoc = "";
       });
   
       $("#Encrypt").click(function() {
           encryptMessage();
       });
   
       $("#Decrypt").click(function() {
           decryptMessage();
       });
   
   });
   ```

5. 后端路由与函数设置：设置根路由与加密函数、解密函数路由

   ```python
   @app.route('/', methods=['GET', 'POST'])
   def home():
       return render_template('index.html')
   
   
   @app.route('/encryptMessage', methods=['GET', 'POST'])
   def encrypt():
       if request.method == 'POST':
           data = request.get_json()
           form = data['form']
           message = data['message']
           # print("明文为: ",message)
           key = data['key']
           keys = getKeys.get_keys(key)       
           message = encryption.PlainTextTransfer(message, form)
           cipher1 = encryption.Cipher(message, keys)
           res = cipher1.transfer()
           res = encryption.CipherTextTransfer(res, form)
           
           # print("密钥为: ",key)
           # print("密文为: ",res)
           return res
       else:
           return "Invalid request method."
       
   
   @app.route('/decryptMessage', methods=['GET', 'POST'])
   def decrypt():
       if request.method == 'POST':
           data = request.get_json()
           form = data['form']
           message = data['message']
           # print("密文为: ",message)
           key = data['key']
           res = deciphering.user_decryption(form,message,key)
           
           # print("密钥为: ",key)
           # print("明文为: ",res)
           return res
       else:
           return "Invalid request method."
   ```

   



#### 4. 暴力破解

##### 4.1 实现单线程暴力破解的函数

输入明文列表plaintext和密文列表ciphertext，先遍历密钥空间，得到能满足第一组明密文对的密钥，放入 valid_keys，再将 valid_keys中的密钥解密第二组，移除解密后与明文不相等的密钥，以此类推，返回所有能满足输入明密文对的密钥。

```python
def brute_force(plaintext, ciphertext):
    length = len(ciphertext)
    i = 0
    valid_keys = []		#记录密钥
    while i < length:
        keys_to_remove = valid_keys[:]	  #记录临时密钥list
        if i == 0:
            for key in range(1024):  # 10位密钥共有2^10种组合
                binary_key = format(key, '010b')  # 将整数密钥转换为10位二进制
                decrypted_text = deciphering.binarystring(ciphertext[i], binary_key)  
                # 使用S-DES解密函数
                if (decrypted_text == plaintext[i]) & (key <= 1024):
                    valid_keys.append(binary_key)
        else:
            for key in keys_to_remove:
                decrypted_text = deciphering.binarystring(ciphertext[i], key)
                if (decrypted_text != plaintext[i]):
                    valid_keys.remove(key)
        i = i + 1
    return valid_keys

```



##### 4.2实现多线程暴力破解的函数

对于每个明文密文对，都会创建一个单独的线程来处理

1.  暴力破解并过滤密钥的函数

    输入明文列表（包含多个明文字符串），密文列表（包含多个密文字符串，与明文对应）。一个列表（用于存储满足特定明文密文对的密钥集合）一个锁对象（用于多线程同步，以确保对共享数据的安全访问）返回当前处理的明文密文对的索引。

    ```python
    def decrypt_and_filter(plaintext, ciphertext, valid_keys, lock, i):
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
    
    ```

2.  多线程暴力破解函数

    该函数的主要作用是使用多线程并行处理多个明文密文对，调用 decrypt_and_filter 函数进行解密和过滤密钥的操作，并返回最终的密钥结果。

    输入明文列表（包含多个明文字符串），密文列表（包含多个密文字符串，与明文对应）返回一个列表，包含满足所有明文密文对的密钥集合。

    ```python
    def brute_force(plaintext, ciphertext):
        "valid_keys = []
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
    
    ```

    







## 用户指南
#### 1.介绍

1.1 什么是S-DES？

欢迎使用S-DES（Simplified Data Encryption Standard）加密工具。S-DES（Simplified Data Encryption Standard）是一种轻量级的对称加密算法，旨在保护数据的机密性。它适用于嵌入式系统和教育用途。

1.2 用户指南概览

本用户指南将帮助您了解如何使用S-DES来加密和解密数据，以及了解有关S-DES的基本原理和安全性考虑。



#### 2.S-DES基础

2.1 S-DES的工作原理

S-DES使用Feistel网络结构，将明文数据分成两半，然后进行一系列的置换和替代操作，最终生成密文。这个过程可以通过反向操作来解密。

2.2 加密和解密

加密：输入明文和密钥，执行加密操作得到密文；

解密：输入密文和正确的密钥，执行解密操作得到明文。

2.3 密钥生成

密钥生成是S-DES中关键的一步。它从10bit密钥生成两个8bit子密钥，用于加密和解密过程。

2.4 GUI界面

<img width="428" alt="image" src="https://github.com/Xialanshan/S_DES/assets/110965468/f8f669eb-ea9b-4c75-b9d4-d2075ad6e749">



#### 3.使用S-DES加密数据

3.1 准备工作

在使用S-DES加密数据之前，您需要：

-   获取一个有效的S-DES密钥（10bit）。

-   准备要加密的明文数据。

3.2 示例：如何使用S-DES加密二进制数据

<img width="411" alt="image" src="https://github.com/Xialanshan/S_DES/assets/110965468/a4cc39fd-1407-4cff-95d9-4870a52ddc17">


3.3 示例：如何使用S-DES加密ASCII字符串

<img width="398" alt="image" src="https://github.com/Xialanshan/S_DES/assets/110965468/f475b733-2691-4357-ba3e-fca82d6895dc">


#### 4.使用S-DES解密数据

4.1 准备工作

在使用S-DES解密数据之前，您需要：

-   获取一个有效的S-DES密钥(10bit)。

-   准备要解密的密文数据。

4.2 示例：如何使用S-DES解密数据

<img width="362" alt="image" src="https://github.com/Xialanshan/S_DES/assets/110965468/6e292772-db74-414e-92f9-673e514c290e">


4.3 示例：如何使用S-DES解密ASCII字符串


<img width="356" alt="image" src="https://github.com/Xialanshan/S_DES/assets/110965468/4c975dfe-15d5-462a-ae4f-ea331c92eb1e">



#### 5.S-DES的参数设置

5.1 密钥长度

S-DES使用二进制10bit密钥

5.2 密钥扩展置换


<img width="318" alt="image" src="https://github.com/Xialanshan/S_DES/assets/110965468/fef85d39-0982-4caf-ae1b-fa4aaadd1f0a">



5.3 初始置换盒

<img width="300" alt="image" src="https://github.com/Xialanshan/S_DES/assets/110965468/0c86fd57-6c6d-4d85-b5a0-e1bbec2eef1c">


5.4 最终置换盒

<img width="296" alt="image" src="https://github.com/Xialanshan/S_DES/assets/110965468/5b7f688e-91d7-4023-b817-8dbfc714eb4f">


5.5 扩展置换盒

<img width="267" alt="image" src="https://github.com/Xialanshan/S_DES/assets/110965468/6e41529e-64df-4af4-a76c-2894344c0984">


5.6替换盒

SBox1:

![image](https://github.com/Xialanshan/S_DES/assets/110965468/0c301247-8a5c-44ac-aaae-5d7f54b253b6)


SBox2:

![image](https://github.com/Xialanshan/S_DES/assets/110965468/5d99bc14-fa64-4a1b-a1ae-59fbd1a6412b)


SPBox:


![image](https://github.com/Xialanshan/S_DES/assets/110965468/9323a4f5-f7e2-4ee2-8cbe-7ccab616f9e1)



#### 6.安全性和注意事项

6.1 S-DES的安全性

S-DES算法的密钥空间相对较小，不是高度安全的加密算法，不适用于处理高度敏感的数据。了解其局限性并采取必要的安全措施。

6.2 密钥管理

密钥的安全存储和分发是使用S-DES时的关键问题。确保密钥不会泄露给未授权的人员。

#### 7.常见问题解答

Q: S-DES与标准DES的区别

A: S-DES是标准DES的简化版本，主要区别在于密钥长度和轮数。标准DES使用56位密钥和16轮Feistel网络运算，更安全但也更复杂。

Q: 为什么我无法解密我的数据

A: 请检查您输入的密钥是否正确，确保与加密时使用的密钥相同。

Q: 我忘记了密钥，如何解密数据？

A: 如果您忘记了密钥，无法解密数据，因为S-DES是对称加密算法，密钥是解密的关键。

Q: 是否有S-DES的编程库或工具？

A: S-DES的编程库和工具可能存在，但不如更现代的加密标准普遍。您可以搜索相关资源或开发自己的S-DES实现。

#### 8.技术支持和反馈

如果您遇到任何问题或需要技术支持，请联系我们的技术支持团队：0123456789\@qq.com

#### 9.附录

9.1 参考文献：

\[1\]\"Cryptography and Network Security: Principles and Practice\" by William Stallings - 本书提供了对S-DES算法的详细说明，以及与计算机网络和信息安全相关的其他内容。

\[2\]\"Cryptography and Network Security: Principles and Practice\" by Behrouz A. Forouzan and Debdeep Mukhopadhyay - 本书涵盖了S-DES算法的基本概念，以及与网络安全和密码学相关的其他主题。

\[3\]\"Introduction to Modern Cryptography: Principles and Protocols\" by Jonathan Katz and Yehuda Lindell - 这本书提供了对S-DES算法的简要介绍，同时还涵盖了现代密码学的其他方面。

\[4\]\"Understanding Cryptography: A Textbook for Students and Practitioners\" by Christof Paar and Jan Pelzl - 本书详细介绍了密码学的基本概念，包括对S-DES算法的讲解。

#### 10.版本历史

版本1.0（2023年10月1日），初始版本。
