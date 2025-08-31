
FROM python:3.12-slim
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
WORKDIR /app
RUN apt-get update && apt-get install -y --no-install-recommends build-essential libpq-dev && rm -rf /var/lib/apt/lists/*
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt
COPY . /app/
ENV DJANGO_SETTINGS_MODULE=alx_backend_caching_property_listings.settings
EXPOSE 8000
CMD sh -c "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"
