from flask import Flask
from flask_socketio import SocketIO, send
import json
# from ..run_predict import runner

def runner(mocker1, mocker2):
    def inner(q, p):
        return {'time' : 0, 
        'scores' : '1002.3, 901.3, 0.0, 0.0',
        'results' : '0'
        }
    return inner

def get_passages(pas_type):
    return "passages"

app = Flask(__name__)

socketio = SocketIO(app)
infer = runner(30, 'empty')


@socketio.on('message')
def response_query(message):
    print(message)
    passages = get_passages(message['passages'])
    result = infer(message['question'], passages)
    send(result, json=True)


if __name__ == '__main__':
    socketio.run(app, debug=True, port=9999)