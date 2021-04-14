import time
from flask import Flask
from datetime import datetime
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World 12!"

@app.route("/status")
def status():
    dt_now = datetime.now()
    return {
        'status': True,
        'name': 'Messenger',
        'time1': time.asctime(),
        'time2': time.time(),
        'time3': dt_now,
        'time4': str(dt_now),
        'time5': dt_now.strftime('%Y/%m/%d time: %H:%M:%S '),
        'time6': dt_now.isoformat()
    }

@app.route("/send", methods=['POST'])
def send_message():
    data = request.json
    name = data['name']
    text = data['text']
    message = {
        'time': time.time(),
        'name': name,
        'text': text
    }
    dp.append(message)

app.run()