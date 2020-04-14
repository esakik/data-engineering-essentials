.PHONY: install
deploy: install
	docker pull jupyter/pyspark-notebook

.PHONY: run
deploy: run
	docker run --rm -p 8888:8888 -v $PWD/data:/home/jovyan/work jupyter/pyspark-notebook start-notebook.sh