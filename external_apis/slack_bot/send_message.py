# See https://slack.dev/python-slackclient/

from flask import current_app
from slack import WebClient
from slack.errors import SlackApiError


slack_client = WebClient(current_app.config['SLACK_BOT_TOKEN'])


def get_channel_by_name(name):
    response = slack_client.conversations_list(
        exclude_archived=1,
        types='public_channel,private_channel'
    )
    if response['ok']:
        channels = response['channels']
        for channel in channels:
            if channel['name'] == name:
                return channel
        return 'Not found, please add the slack bot in the channel'
    return 'Error'

def send(message, receiver_name):
    try:
        receiver = get_channel_by_name(receiver_name)
        if receiver not in ('Error',  'Not found'):
            receiver_id = receiver['id']
            slack_client.chat_postMessage(
                channel=receiver_id,
                text=message
            )
            return 'Send'
        return receiver
    except SlackApiError as e:
        # You will get a SlackApiError if "ok" is False
        assert e.response["ok"] is False
        assert e.response["error"]  # str like 'invalid_auth', 'channel_not_found'
        return e.response["error"]
