# coding:utf-8
import json
import sys

import boto3

sys.path.append("./site-packages")


def lambda_handler(event, context):
    """ Lambda Handler

    :param event:
    :param context:
    """

    import slackweb

    del context

    boto_s3 = boto3.resource("s3")
    obj = boto_s3.Object("kikusu-config", "slack/kikusu-incoming-webhook.json")

    slack_url = json.load(obj.get()["Body"])["url"]
    message = json.loads(event['Records'][0]['Sns']['Message'])

    alarm_name = message['AlarmName']
    new_state = message['NewStateValue']
    reason = message['NewStateReason']

    slack = slackweb.Slack(slack_url)
    slack.notify(
        attachments=[
            dict(
                title=alarm_name,
                author_name="cloudwatch",
                fields=[
                    dict(title="NewState", value=new_state),
                    dict(title="Reason", value=reason),
                ],
                color="warning"),
        ],
        icon_emoji=":cloudwatch:"
    )


