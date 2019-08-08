# -*- encoding:utf-8 -*-
from flask import Flask

app = Flask(__name__)

#------------转换器---------
#转换器默认为字符型
@app.route('/<name>/')
def show_string(name):
    return "show_string：%s" %name

@app.route('/<int:postId>/')
def show_int(postId):
    return "show_int：%d" %postId

@app.route('/<float:myNo>/')
def show_float(myNo):
    return "show_float：%f" %myNo

@app.route('/<path:url>/')#斜杠转换器
def show_url(url):
    return "show_url：%s"%url

if __name__ == '__main__':
    app.run(debug=True)
