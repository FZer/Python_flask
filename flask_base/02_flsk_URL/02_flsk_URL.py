# -*- encoding:utf-8 -*-
from flask import Flask
from flask import redirect
from flask import url_for

app = Flask(__name__)

@app.route('/wel_admin/')
def hello_admin():
    return "Hello Admin"

@app.route('/wel_guest/<name01>/')
def hello_guest(name01):
    return "Hello %s as Guest" %name01

"""
hello_user()函数检查接收的参数是否与'admin'匹配。如果匹配，则使用url_for()将应用程序重定向到hello_admin()函数，
否则重定向到将接收的参数作为name01参数,传递给它的hello_guest()函数。
"""
@app.route('/user/<name>/')
def hello_user(name):
    if name == 'admin':
        return redirect(url_for('hello_admin'))
    else:
        return redirect(url_for('hello_guest',name01 = name))

if __name__ == '__main__':
    app.run(debug=True)