FROM python:3.7

RUN pip install pymongo requests-oauthlib tqdm python-dotenv

ENV ON_DOCKER true

WORKDIR /app
ADD twitter2mongo.py /app/
ADD .env /app/
CMD ["python", "/app/twitter2mongo.py", "--keyword=Python", "--max_counts=10"]
