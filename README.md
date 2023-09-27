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


## 用户指南

