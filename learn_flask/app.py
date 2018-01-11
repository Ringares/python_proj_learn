#!/usr/bin/env python3
""""
DOC:
http://flask.pocoo.org

RESTFUL API:
http://www.pythondoc.com/flask-restful/third.html#id1

WEBSITE:
https://www.jianshu.com/p/cc90a14856c5
"""
from flask import Flask, jsonify, abort
from flask import make_response
from flask import request

# from flask import Response

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    }
]


@app.route('/todo/api/v1/0/tasks', methods=['POST'])
def create_task():
    if not request.json or not 'title' in request.json:
        abort(404)

    task = {
        'id': tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json['description'],
        'done': False
    }
    tasks.append(task)
    return jsonify({'task': task}), 201


@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})


@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = list(filter(lambda t: t['id'] == task_id, tasks))
    if len(task) == 0:
        raise MyException('channel_1')
        # abort(404)
        # abort(Response('Hello World'))
    return jsonify({'task': task[0]})


@app.route('/')
def index():
    return 'Hello World'


class MyException(Exception):
    status_code = 555

    def __init__(self, channel_name=None):
        self.channel_name = channel_name

    def __str__(self):
        return 'pull channel {channel_name} data exception. ' \
               '(maybe caused by umeng api restriction, try 15mins later.)'.format(
            channel_name=self.channel_name)

    def to_dict(self):
        rv = dict()
        rv['message'] = self.__str__()
        rv['status'] = self.status_code
        return rv


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found', 'desc': str(error)}), 404)


@app.errorhandler(MyException)
def handle_exception(error):
    response = jsonify(error.to_dict())
    response.status_code = 404
    return response


if __name__ == '__main__':
    app.run(debug=True)
