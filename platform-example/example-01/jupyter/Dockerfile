FROM python:3.7

RUN pip install jupyter pandas pymongo

WORKDIR /app
ADD start.sh /app/
CMD ["bash", "/app/start.sh"]
