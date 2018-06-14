# -*- coding: utf-8 -*-
from hurry.app import Hurry

app = Hurry()

@app.get('/api/success')
def hello_world(req, res):
    res.status(200)

@app.get('/api/error/400')
def hello(req, res):
    res.status(400)

@app.get('/api/error/500')
def hello(req, res):
    res.status(500)

if __name__ == '__main__':
    app.run()
