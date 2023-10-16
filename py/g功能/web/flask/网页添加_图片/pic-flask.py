#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    wz1 = "https://img1.baidu.com/it/u=2292210371,42019104&fm=253&fmt=auto&app=138&f=JPEG?w=380&h=242"
    return render_template('index.html', image_url='example.jpg',tpwz=wz1)

if __name__ == '__main__':
    app.debug = True
    app.run()
