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
