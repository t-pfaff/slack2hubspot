#!/usr/bin/env python
# encoding: utf-8

from bottle import run, post
import os

@post('/contact')
def contact():
    return 'Hello World!'

port = int(os.environ.get('PORT', 5000))

if __name__ == '__main__':
    run(host='0.0.0.0', port=port)