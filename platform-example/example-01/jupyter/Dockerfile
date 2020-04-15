FROM jupyter/pyspark-notebook

RUN pip install pymongo

WORKDIR /app
ADD start.sh /app/
CMD ["bash", "/app/start.sh"]
