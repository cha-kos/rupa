from django.test import SimpleTestCase
from .serializers import EmailSerializer
from .backends import MailGunClient, SendGridClient

REQUEST_DATA = {
    'to_email': 'mailman@mail.com',
    'to_name': 'Mail Man',
    'from_email': 'notmailmain@mail.com',
    'from_name': 'Not Mail Man',
    'subject': 'This is the subject',
    'body': '<h1>Your Bill</h1><p>$10</p>'
}


class EmailSerializerTest(SimpleTestCase):
    def test_body_field_removes_html(self):
        serializer = EmailSerializer(data=REQUEST_DATA)
        serializer.is_valid()
        self.assertEqual(serializer.validated_data.get('body'), 'Your Bill\n$10')


class MailGunClientTest(SimpleTestCase):
    def test_build_request_data(self):
        client = MailGunClient()
        client.build_request_data(REQUEST_DATA)
        self.assertEqual(client.payload, {
            'from': 'Not Mail Man <notmailmain@mail.com>',
            'to': ['Mail Man <mailman@mail.com>'],
            'subject': 'This is the subject',
            'text': '<h1>Your Bill</h1><p>$10</p>'
        })


class SendGridClientTest(SimpleTestCase):
    def test_build_request_data(self):
        client = SendGridClient()
        client.build_request_data(REQUEST_DATA)
        self.assertEqual(client.payload, {
            'personalizations': [{
                'to': [{'email': 'mailman@mail.com', 'name': 'Mail Man'}]
            }],
            'from': {'email': 'notmailmain@mail.com', 'name': 'Not Mail Man'},
            'subject': 'This is the subject',
            'content': [{'type': 'text/plain', 'value': '<h1>Your Bill</h1><p>$10</p>'}]})
