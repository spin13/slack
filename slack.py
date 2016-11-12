
import env
import requests


SLACK_TOKEN = env.SLACK_TOKEN

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
