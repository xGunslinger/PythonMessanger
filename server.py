from flask import Flask, request, abort
from datetime import datetime
import time

app = Flask(__name__)
messages = [
    {'name': 'Jack', 'time': time.time(), 'text': '123'},
    {'name': 'Jack', 'time': time.time(), 'text': '1234'},
]
users = {
    'Jack': '12345'
}


@app.route("/")
def hello_view():
    return 'Hello, World! <a href="/status">Статус</a>'


def counter(elements):
    count = 0
    for element in elements:
        count += 1
    return count

@app.route("/status")
def status_view():
    return {
        'status': True,
        'users': counter(users),
        'messages': counter(messages),
        'name': 'ABC',
        'time0': datetime.now(),
        'time1': datetime.now().isoformat(),
        'time2': datetime.now().strftime('Hi %Y/%m/%d %H:%M:%S'),
        'time3': time.time(),
        'time4': time.asctime()
    }


@app.route("/send", methods=['POST'])
def send_view():
    name = request.json.get('name')
    password = request.json.get('password')
    text = request.json.get('text')

    for token in [name, password, text]:
        if not isinstance(token, str) or not token or len(token) > 1024:
            abort(400)

    if name in users:
        # auth
        if users[name] != password:
            abort(401)
    else:
        # sign up
        users[name] = password

    messages.append({'name': name, 'text': text, 'time': time.time()})
    return {'ok': True}



def filter_dicts(elements, key, min_value):
    new_elements = []

    for element in elements:
        if element[key] > min_value:
            new_elements.append(element)

    return new_elements


@app.route("/messages")
def messages_view():
    try:
        after = float(request.args['after'])
    except:
        abort(400)
    filtered_messages = filter_dicts(messages, key='time', min_value=after)
    return {'messages': filtered_messages}


app.run()
