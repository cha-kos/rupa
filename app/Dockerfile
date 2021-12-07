# LOCAL dev dockerfile, does not support deployment.
FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH $PYTHONPATH:/app
ENV PYTHONPATH $PYTHONPATH:/app/api
ENV DJANGO_SETTINGS_MODULE api.settings
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt