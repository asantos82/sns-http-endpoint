from flask import Flask, request
import requests
import json

app = Flask(__name__)

def msg_process(msg, tstamp):
    js = json.loads(msg)
    msg = 'Region: {0} / Alarm: {1}'.format(
        js['Region'], js['AlarmName']
    )
    # do stuff here, like calling your favorite SMS gateway API
    print('HERE2')
    json_formatted_str = json.dumps(js, indent=2)
    print(json_formatted_str)

@app.route('/', methods = ['GET', 'POST', 'PUT'])
def sns():
    print request.__dict__
    # AWS sends JSON with text/plain mimetype
    try:
        js = json.loads(request.data)
        print('HERE')
        json_formatted_str = json.dumps(js, indent=2)
        print(json_formatted_str)
    except:
        pass

    hdr = request.headers.get('X-Amz-Sns-Message-Type')
    # subscribe to the SNS topic
    if hdr == 'SubscriptionConfirmation' and 'SubscribeURL' in js:
        r = requests.get(js['SubscribeURL'])

    if hdr == 'Notification':
        msg_process(js['Message'], js['Timestamp'])

    return 'OK\n'

if __name__ == '__main__':
    app.run(
        host = "0.0.0.0",
        port = 5000,
        debug = True
    )
