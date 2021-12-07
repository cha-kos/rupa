from django.conf import settings
import requests
import utils


class EmailClient():
    auth_type = 'basic'  # or bearer

    def __init__(self, *args, **kwargs):
        self.key = kwargs.get('key', None)
        self.endpoint = kwargs.get('endpoint', None)

    def send_mail(self, data):
        self.build_request_data(data)
        return self.perform_request()

    def build_request_data(self, data):
        # define on specific client class
        pass

    def perform_request(self):
        return getattr(utils, f'post_{self.auth_type}_auth')(
            key=self.key,
            endpoint=self.endpoint,
            payload=self.payload,
            user=getattr(self, 'user', None),
        )


class MailGunClient(EmailClient):
    auth_type = 'basic'
    user = 'api'

    def build_request_data(self, data):
        self.payload = {
            'from': '{} <{}>'.format(data['from_name'], data['from_email']),
            'to': ['{} <{}>'.format(data['to_name'], data['to_email'])],
            'subject': data['subject'],
            'text': data['body']
        }


class SendGridClient(EmailClient):
    auth_type = 'bearer'

    def build_request_data(self, data):
        self.payload = {
            "personalizations": [{
                "to": [{
                    "email": data['to_email'],
                    "name": data['to_name']
                }]
            }],
            "from": {
                "email": data['from_email'],
                "name": data['from_name']
            },
            "subject": data['subject'],
            "content": [{
                "type": "text/plain",
                "value": data['body']
            }],
        }
