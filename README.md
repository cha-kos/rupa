# Rupa Coding Challenge

## Requirements
This app requires [Docker](https://docs.docker.com/get-docker/)
For linux users, [Docker Compose](https://docs.docker.com/compose/install/) is also required since it does not come prepackaged in Docker like Mac and Windows

### Local Development
To develop locally run the command `./run.sh local` from within the root directory of this repo. The server will be running locally on port 8000. You can make POST requests to send email at `localhost:8000/messaging/email/`
#### Environment Configuration
An environment file template can found in `/app/.env.example`. Copy this file into a new file named `.env.development` and populate with your credentials for sending email through MailGun and SendGrid

### Local Testing
To run test locally run the command `./run.sh test` from within the root directory of this repo

## Solution
For my solution I chose to work in Python within the Django framework as I felt it was suitable for this challenge of providing an api endpoint to send email. 

Additional Python Libraries used for completing this challenge include
- [Django Rest Framework](https://www.django-rest-framework.org/) for writing an api view and validating request data
- [requests](https://docs.python-requests.org/en/latest/) for making simple POST requests
- [beautifulsoup](https://beautiful-soup-4.readthedocs.io/en/latest/) for parsing html into clean readable plain text

### Tradeoffs etc.
- Handling of the incoming request object with the `from` attribute. Usually I write DRF serializers to be one to one with request body, but since `from` is a reserved word in Python I simply changed this att to `from_email` inside of the view (and subsequently `to_email` for consistency), before sending off to the serializer for validation. I would probably request that the endpoint requirements change that attribute to `from_email` rather than `from`.
- I did not write any tests e2e tests to test the functionality of making the api calls and triggering a fallback. If I were to spend more time on this project, I would whip up some mock api calls and test the fucntionality of the email client fallback.
- If I were to spend more time on this project I would built out support for html formatted email body to populate fields for both plaintext and html.
- In the case of deploying to production I would implement a task queue to send emails with [celery](https://docs.celeryproject.org/en/stable/)

I spent about 4 hours total on this project, give or take as I chipped away at it over the week time span. 
