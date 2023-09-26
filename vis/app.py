from flask import Flask, request, render_template
from flask import request
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import encryption
import getKeys
import deciphering

app = Flask(__name__)

templates_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
app.template_folder = templates_dir     # 设定相对路径,导入.html文件

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


if __name__=="__main__":
    app.run()