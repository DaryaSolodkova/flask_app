FROM python:3.9.2-alpine

LABEL maintainer="dashasolodkova@gmail.com"
LABEL description="Print Python version"

EXPOSE 80

VOLUME /flask_data

WORKDIR /app

COPY . /app

RUN apk update && apk upgrade
RUN pip install -r requirements.txt

# ENTRYPOINT ["python", "server.py"]
CMD ["python", "server.py"]

