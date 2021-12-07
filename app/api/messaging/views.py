# from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http import HttpResponse
from django.conf import settings
from .serializers import EmailSerializer
from .backends import MailGunClient, SendGridClient


@api_view(['POST'])
def send_email(request):
    data = request.data
    # handle request data for python reserved word: from
    data['from_email'] = data.get('from', None)
    data['to_email'] = data.get('to', None)
    serializer = EmailSerializer(data=data)
    serializer.is_valid(raise_exception=True)

    service_providers = [
        MailGunClient(
            key=settings.MAILGUN_API_KEY,
            endpoint=settings.MAILGUN_ENDPOINT
        ),
        SendGridClient(
            key=settings.SENDGRID_API_KEY,
            endpoint=settings.SENDGRID_ENDPOINT
        )
    ]
    for service_provider in service_providers:
        response = service_provider.send_mail(serializer.validated_data)
        if response.status_code == 200 or response.status_code == 202:
            return HttpResponse('SUCCESS: Email Sent via {}'.format(service_provider.__class__.__name__))
        else:
            print('ERROR: Email Failed via {}'.format(service_provider.__class__.__name__))
