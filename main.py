import os
import traceback

from flask import Flask, jsonify, Response
from SciHub import driver
from app import app

@app.route('/')
def hello():
    return 'Hello!!'

@app.route('/test/', methods=['GET'])
def go_headless():
    try:
        driver.get("https://techwithtim.net")
        title = driver.title
        driver.close()
        return jsonify({'success': True, "result": title})
    except Exception as e:
        print(traceback.format_exc())
        return jsonify({'success': False, 'msg': str(e)})

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)