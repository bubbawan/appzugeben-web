from flask import jsonify, request, redirect
from app import app
import os

@app.route('/')
@app.route('/index')
def index():
    return 'appzugeben'

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    fileU = request.files['file']
    fileU.save(os.path.join(app.config['UPLOAD_FOLDER'], 'hello.jpg'))
    return redirect('/index')
            
@app.route('/user/check')
def checkUser():
    result = dict()
    result['deviceId'] = '231982731'
    result['result'] = 'ok'
    return jsonify(result)

@app.route('/user/add', methods=['GET', 'POST'])
def addUser():
    result = dict()
    result['deviceId'] = '231982731'
    result['result'] = 'ok'
    result['info'] = 'user added'
    return jsonify(result)

@app.route('/user/update', methods=['GET', 'POST'])
def updateUser():
    result = dict()
    result['deviceId'] = '231982731'
    result['result'] = 'ok'
    result['info'] = 'user updated'
    return jsonify(result)

@app.route('/anzeige/add', methods=['GET', 'POST'])
def addAnzeige():
    result = dict()
    result['deviceId'] = '231982731'
    result['anzeigeId'] = 'anzeigeXYZ'
    result['result'] = 'ok'
    return jsonify(result)

@app.route('/anzeige/remove', methods=['GET', 'POST'])
def removeAnzeige():
    result = dict()
    result['deviceId'] = '231982731'
    result['anzeigeId'] = 'anzeigeXYZ'
    result['result'] = 'ok'
    return jsonify(result)

@app.route('/anzeige/update', methods=['GET', 'POST'])
def updateAnzeige():
    result = dict()
    result['deviceId'] = '231982731'
    result['anzeigeId'] = 'anzeigeXYZ'
    result['result'] = 'ok'
    return jsonify(result)

@app.route('/message/send', methods=['GET', 'POST'])
def sendMessage():
    result = dict()
    result['deviceId'] = '231982731'
    result['anzeigeId'] = 'anzeigeXYZ'
    result['result'] = 'sent message'
    return jsonify(result)

@app.route('/message/get', methods=['GET', 'POST'])
def getMessages():
    result = dict()
    result['deviceId'] = '231982731'
    result['anzeigeId'] = 'anzeigeXYZ'
    result['result'] = 'got messages'
    return jsonify(result)