
import env
import requests
import json

SLACK_TOKEN = env.SLACK_TOKEN
APP_TOKEN = env.APP_TOKEN

def post_slack(username='', channel='', message=''):
    url = 'https://slack.com/api/chat.postMessage'
    params ={
        'token': SLACK_TOKEN,
        'channel': channel,
        'text': message,
        'username': username
    }
    res = requests.post(url, params=params)
    return res

def message_button():
    attachments = [
        {
            'fallback': 'fallback',
            'text': 'text',
            'callback_id': 'callback_id',
            'color': '#EE2222',
            'attachment_type': 'default',
            'actions': [
                {
                    'name': 'name1',
                    'text': 'tetx1',
                    'type': 'button',
                    'value': 'value1'
                },{
                    'name': 'name2',
                    'text': 'tetx2',
                    'type': 'button',
                    'value': 'value2'
                }
            ]
        },{
            'fallback': 'fallback',
            'text': 'text',
            'callback_id': 'callback_id',
            'color': '#EE2222',
            'attachment_type': 'default',
            'actions': [
                {
                    'name': 'name1',
                    'text': 'tetx1',
                    'type': 'button',
                    'value': 'value1'
                },{
                    'name': 'name2',
                    'text': 'tetx2',
                    'type': 'button',
                    'value': 'value2'
                }
            ]
        }
    ]

    payload = {
        'token': APP_TOKEN,
        'channel': '#dev_null',
        'username': 'button_man',
        'attachments': json.dumps(attachments)
    }
    url = 'https://slack.com/api/chat.postMessage'
    requests.post(url, data=payload)


if __name__ == '__main__':
    message_button()

