# -*- encoding:utf-8 -*-
from flask import Flask
from flask import redirect
from flask import url_for
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route('/')
def http_index():
    return render_template('test01.html')

@app.route('/success_post/<name01>/')
def form_post(name01):
    return "POST: %s" %name01

@app.route('/success_get/<name02>/')
def form_get(name02):
    return "GET: %s" %name02
    
@app.route('/index/',methods = ['POST','GET'])#表单的action的url必须和路由转换的地址一致；如'/index/'结尾都带有 '/',或者都不带。
def index():
    if request.method == 'POST':
        user = request.form['username']
        return redirect(url_for('form_post',name01 = user))
    else:
        user = request.args.get('username')
        return redirect(url_for('form_get',name02 = user))

if __name__ == '__main__':
    app.run(host="127.0.0.2",port=8088,debug=True)