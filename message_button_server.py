# -*- coding: utf-8 -*-

import os, sys
from bottle import Bottle, route, run, request, server_names, ServerAdapter
sys.path.append('./wunderlist')

import requests
import json
import slack
import wunderlist_api
import env

SLACK_WUNDERLIST_TOKENS = env.SLACK_WUNDERLIST_TOKENS

@route('/', method='POST')
def index():
    params = json.loads(request.params.payload)
    fallback = params['original_message']['attachments'][0]['fallback']
    action = params['actions'][0]
    callback = params['callback_id']

    mess = ''
    if 'wunderlist' == fallback:
        mess = wunderlist(callback=callback, actions=action)
    return mess



@route('/wunderlist', method='POST')
def wunderlist_end_point():
    channel = request.params.channel_name
    text = request.params.text.split(' ')
    sess = wunderlist_api.create_session()
    project_id = wunderlist_api.get_project_id_by_name(sess, name=channel)

    if 'list' == text[0]:
        wunderlist_api.post_task_list(sess, channel='#' + channel, project_id=project_id)
    if 'add' == text[0]:
        jp = text[1]
        due = ''
        if len(text) == 3:
            due = text[2]
        wunderlist_api.add_task(sess, task=jp, due_date=due, project_id=project_id)
        wunderlist_api.post_task_list(sess, channel='#' + channel, project_id=project_id)
    sess.close()

# wunderlistの処理
def wunderlist(callback='', actions=''):
    sess = wunderlist_api.create_session()
    js = json.loads(request.params.payload)
    channel = js['channel']['name']
    project_id = wunderlist_api.get_project_id_by_name(sess, name=channel)
    ret = ''
    print('wunderlist task complete')
    if callback == 'task':
        rev = wunderlist_api.get_task_revision(sess, actions['value'])
        ret = wunderlist_api.complete_task(sess, actions['value'], rev)
        wunderlist_api.post_task_list(sess, channel='#' + channel, project_id=project_id)
    sess.close()
    return ret
run(host='0.0.0.0', port=5000, debug=True, reloader=True)
