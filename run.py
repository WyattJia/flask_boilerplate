# -*- coding:utf-8 -*-
"""
    flask_boilerplate_master.py

    :run application on debug
"""

from flask_boilerplate import create_app
from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop

app = create_app('config.cfg')

server = HTTPServer(WSGIContainer(app))

if __name__ == '__main__':
    app.run(debug=True)
