#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from flask import Flask, request

app = Flask(__name__)

@app.route('/api/get')

def testGet():
    
    name = request.args.get('name')
    ('name')

    print(name)
    return name + "是大哥！"

if __name__ == '__main__':
    app.run()