# -*- encoding:utf-8 -*-
from flask import Flask
from flask import redirect
from flask import url_for
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route('/index/')
def http_index():
    return render_template('index.html')

@app.route('/success/<name01>/')
def success(name01):
    return "welcome %s" %name01

    
@app.route('/index/',methods = ['POST','GET'])#表单的action的url必须和路由转换的地址一致；如'/index/'结尾都带有 '/',或者都不带。
def index():
    if request.method == 'POST':
        user = request.form['username']
        return redirect(url_for('success',name01 = user))
    else:
        user = request.args.get('username')
        return redirect(url_for('success',name = user))

if __name__ == '__main__':
    app.run(host="127.0.0.2",port=8088,debug=True)